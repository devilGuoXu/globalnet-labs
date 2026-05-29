// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://devilGuoXu.github.io',
  base: '/globalnet-labs',
  vite: {
    plugins: [tailwindcss()]
  }
});