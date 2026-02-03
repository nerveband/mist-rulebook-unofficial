// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import beautifulMermaid from 'starlight-beautiful-mermaid';
import starlightScrollToTop from 'starlight-scroll-to-top';
import starlightSidebarSwipe from 'starlight-sidebar-swipe';
import starlightVideos from 'starlight-videos';

export default defineConfig({
	integrations: [
		beautifulMermaid(),
		starlight({
			title: 'MIST Rulebook',
			description: 'Unofficial MIST 2026 Competition Rulebook',
			plugins: [
				starlightScrollToTop(),
				starlightSidebarSwipe(),
				starlightVideos(),
			],
			components: {
				Head: './src/components/Head.astro',
			},
			social: [
				{ icon: 'external', label: 'Official MIST Site', href: 'https://getmistified.com' },
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/nerveband/mist-rulebook-unofficial' },
			],
			customCss: ['./src/styles/custom.css'],
			head: [
				{
					tag: 'meta',
					attrs: {
						name: 'og:image',
						content: '/og-image.png',
					},
				},
			],
			sidebar: [
				{ label: 'Home', link: '/' },
				{
					label: "What's New in 2026",
					link: '/changes/2026/',
					badge: { text: 'New', variant: 'tip' },
				},
				{
					label: 'Quick Start Guides',
					items: [
						{ label: 'For Students', link: '/guides/for-students/' },
						{ label: 'For Coaches', link: '/guides/for-coaches/' },
						{ label: 'For Judges', link: '/guides/for-judges/' },
					],
				},
				{
					label: 'Resources',
					items: [
						{ label: 'Knowledge Test Books', link: '/knowledge-test-books/' },
						{
							label: 'Quiz Bowl Topics',
							autogenerate: { directory: 'quiz-bowl-topics' },
						},
						{ label: 'Debate Topics', link: '/debate-topics/' },
						{ label: 'Glossary', link: '/glossary/' },
						{ label: 'PDFs', link: '/resources/' },
					],
				},
				{
					label: 'Rulebook',
					items: [
						{ label: 'Theme & Honor Code', link: '/rulebook/theme-honor-code/' },
						{ label: 'Tournament Guidelines', link: '/rulebook/tournament-guidelines/' },
						{ label: 'Competitor Guidelines', link: '/rulebook/competitor-guidelines/' },
						{ label: 'Audience Guidelines', link: '/rulebook/audience-guidelines/' },
						{ label: 'Early Submissions', link: '/rulebook/early-submissions/' },
						{
							label: 'Knowledge & Quran',
							autogenerate: { directory: 'rulebook/knowledge-quran' },
						},
						{
							label: 'Arts',
							autogenerate: { directory: 'rulebook/arts' },
						},
						{
							label: 'Writing & Oratory',
							autogenerate: { directory: 'rulebook/writing-oratory' },
						},
						{
							label: 'Brackets',
							autogenerate: { directory: 'rulebook/brackets' },
						},
						{
							label: 'Group Projects',
							autogenerate: { directory: 'rulebook/group-projects' },
						},
						{
							label: 'Sports',
							autogenerate: { directory: 'rulebook/sports' },
						},
					],
				},
				{
					label: 'Regional Rules',
					badge: { text: 'Pilot', variant: 'note' },
					items: [
						{
							label: 'Nashville',
							autogenerate: { directory: 'regions/nashville' },
						},
					],
				},
			],
		}),
	],
});
