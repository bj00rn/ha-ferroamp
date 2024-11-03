# Changelog

## [2.0.0](https://github.com/bj00rn/ha-ferroamp/compare/v1.15.0...v2.0.0) (2024-11-03)


### ⚠ BREAKING CHANGES

* Requires Home Assistant 2021.8

### Features

* add config and option flow, multiple hubs ([958b8c7](https://github.com/bj00rn/ha-ferroamp/commit/958b8c71a562de9ca3acd4d729ca41cec099f33e))
* add ESM status sensor ([d3d6218](https://github.com/bj00rn/ha-ferroamp/commit/d3d6218362bc3b04bf3cb9bb9fdb5c8af4a07b67)), closes [#24](https://github.com/bj00rn/ha-ferroamp/issues/24)
* add last_reset to battery energy sensors ([dc5d21f](https://github.com/bj00rn/ha-ferroamp/commit/dc5d21ff1051f4bbc12af6d26bab40fa794580e4))
* add missing ESM Rated Power sensor ([8af545c](https://github.com/bj00rn/ha-ferroamp/commit/8af545cf9d4e08504f41060234385b72b23706a3))
* add missing sensor for Adaptive Current Equalization ([483c21c](https://github.com/bj00rn/ha-ferroamp/commit/483c21c4d082f8a3be84370615610449e3327442))
* add option for frequency precision ([631f700](https://github.com/bj00rn/ha-ferroamp/commit/631f700be8848d8149cbf276600912709da30e5f))
* add release workflow ([b95acfb](https://github.com/bj00rn/ha-ferroamp/commit/b95acfb0d91afdaecac07028d5a3e3e09d910d6a))
* add selectors to services and add tests ([7fe6c66](https://github.com/bj00rn/ha-ferroamp/commit/7fe6c66b0730d9161ce8e6d82c933b4ff6c0e2e1))
* add sensor for estimated grid frequency ([ce5fedc](https://github.com/bj00rn/ha-ferroamp/commit/ce5fedcdb6123505ae783a8ccc744048d2a16ac3)), closes [#19](https://github.com/bj00rn/ha-ferroamp/issues/19)
* add sensor for extapi version ([bc0ac4f](https://github.com/bj00rn/ha-ferroamp/commit/bc0ac4f4dcfba0ccbfa7b5d92787b564552046fc))
* add sensor for last command and status ([47b9fee](https://github.com/bj00rn/ha-ferroamp/commit/47b9feeaedac1047663b82c46882d3beac1a24f6))
* add sensor for load balancing ([1457341](https://github.com/bj00rn/ha-ferroamp/commit/1457341477c0630c196e1b1f05ed62643d44e0f8))
* add sensors used for load balancing applications. ([76cb1e1](https://github.com/bj00rn/ha-ferroamp/commit/76cb1e1cb59e01f4951d011942588af033c55d88))
* add separate entities per phase ([1a77b29](https://github.com/bj00rn/ha-ferroamp/commit/1a77b29cf6828a766e6ed862eaac6c77e65ee813)), closes [#353](https://github.com/bj00rn/ha-ferroamp/issues/353)
* add SSO fault codes ([1005637](https://github.com/bj00rn/ha-ferroamp/commit/10056371bf328cc589f07a6dfa8335ff5d954885))
* add support for Home Assistant Home Energy Management ([3ed3b38](https://github.com/bj00rn/ha-ferroamp/commit/3ed3b380714b571964dfb40dde417d2a85263f45))
* add support for long-term statistics to SSO energy sensor ([38a506c](https://github.com/bj00rn/ha-ferroamp/commit/38a506c7e743e49b5059ac767ea54bf6e7d41c26)), closes [#70](https://github.com/bj00rn/ha-ferroamp/issues/70)
* add textual representation of ESO faultcodes as attributes ([356da52](https://github.com/bj00rn/ha-ferroamp/commit/356da5294f5ca23423fe6eebfedfa016fbe4fec1))
* added possibility to turn on debug logging of events ([c019991](https://github.com/bj00rn/ha-ferroamp/commit/c019991487cacd448bb541bbe01f1b74f3ac1741))
* change default precisions and make them configurable ([b7918ec](https://github.com/bj00rn/ha-ferroamp/commit/b7918eca7d36291c7243fbcc1096cc0956ec0cc6)), closes [#16](https://github.com/bj00rn/ha-ferroamp/issues/16)
* change name for hacs.yaml ([4611fdd](https://github.com/bj00rn/ha-ferroamp/commit/4611fddb10ee61a9364584b955dff9dece4e2343))
* **changelog:** add custom sections for changelog types ([35112a4](https://github.com/bj00rn/ha-ferroamp/commit/35112a4d613bb753c7abbbd830cc8b22d32e2e3f))
* **ci:** add github action to run pre-commit ([f8296ce](https://github.com/bj00rn/ha-ferroamp/commit/f8296ce73ce506a177999dfefeb3490fde457784))
* make sure MQTT integration is loaded before setup ([704919c](https://github.com/bj00rn/ha-ferroamp/commit/704919c682b86969b617515cdd255c8b93c64b7a))
* make sure state is always increasing for energy sensors ([d389ca1](https://github.com/bj00rn/ha-ferroamp/commit/d389ca10a2d4b7ebdfa17894f0c68eadf336c23b)), closes [#76](https://github.com/bj00rn/ha-ferroamp/issues/76)
* make sure that 3-phase energy sensors are strictly increasing ([9446217](https://github.com/bj00rn/ha-ferroamp/commit/9446217e2b949069a30c98fbf97e2bf073ddc143)), closes [#126](https://github.com/bj00rn/ha-ferroamp/issues/126)
* migrate to new entity naming style ([b801eb6](https://github.com/bj00rn/ha-ferroamp/commit/b801eb669aba32b8afea5eec10f0d6fe0b709437))
* only add sensors for loadbalancing if present in message ([6bac6eb](https://github.com/bj00rn/ha-ferroamp/commit/6bac6eb627c8dc48fe2e3d0a2cedaca325992a1f)), closes [#292](https://github.com/bj00rn/ha-ferroamp/issues/292)
* remove integration name from sensor names ([a15ec5a](https://github.com/bj00rn/ha-ferroamp/commit/a15ec5a8778c7bfe4046ba1eb875fa813b8c4887)), closes [#49](https://github.com/bj00rn/ha-ferroamp/issues/49)
* remove model-info from SSO-name ([cebf601](https://github.com/bj00rn/ha-ferroamp/commit/cebf6015d1e9666a91b29fc9868cf38a05fe03c7)), closes [#26](https://github.com/bj00rn/ha-ferroamp/issues/26)
* remove precision config since now builtin to HA ([894dea6](https://github.com/bj00rn/ha-ferroamp/commit/894dea672ad98b5a9d7fcf91186f0b1cb7090ca0))
* requirements for hacs default ([a8dfee1](https://github.com/bj00rn/ha-ferroamp/commit/a8dfee107a9a5183a112fb303f0cc84914f1b368))
* trim ESM name to just serial number ([df38d8f](https://github.com/bj00rn/ha-ferroamp/commit/df38d8fb114cc38696a3c7ff81b451502231e47f))
* update to HA 2021.7 and use entity attrs ([15617a6](https://github.com/bj00rn/ha-ferroamp/commit/15617a6a0f8014ab339537e405df58fdb21e6349))
* updated to support Home Assistant 2021.12 ([217e933](https://github.com/bj00rn/ha-ferroamp/commit/217e933d49d1cacf65ba1bc28d468e0f393b89e0))
* updated to support Home Assistant 2021.9 long term stats ([e13f414](https://github.com/bj00rn/ha-ferroamp/commit/e13f4146a4c95915420935c485414f8194380c57))
* updating readme.md ([db615b2](https://github.com/bj00rn/ha-ferroamp/commit/db615b274e297d70fd93099181618a1efbce1007))
* vscode devcontainer configuration ([be15b07](https://github.com/bj00rn/ha-ferroamp/commit/be15b0710dad8b0146cceaccb8bd8abeb431482e))


### Bug Fixes

* add additional SSO fault codes ([a535c10](https://github.com/bj00rn/ha-ferroamp/commit/a535c1078cf2960382125163402b322f30342859)), closes [#361](https://github.com/bj00rn/ha-ferroamp/issues/361)
* add control status sensor on init ([2beb9b1](https://github.com/bj00rn/ha-ferroamp/commit/2beb9b15e0c9a19f7217a74bf6ea6b4cd77e095d)), closes [#330](https://github.com/bj00rn/ha-ferroamp/issues/330)
* add name to service fields ([c5c5430](https://github.com/bj00rn/ha-ferroamp/commit/c5c54306d46687bda2710d244cf0d03453d93769))
* add wait_background_tasks parameter to block_till_done function ([1e3fb60](https://github.com/bj00rn/ha-ferroamp/commit/1e3fb60dbbbe500cbd587eb7b82413e44239ba16))
* average calculation ([391e563](https://github.com/bj00rn/ha-ferroamp/commit/391e563d509ac8fc07a1ce9442f6c9c073804dca))
* battery icon not shown when below 10 percent ([dd7a8a5](https://github.com/bj00rn/ha-ferroamp/commit/dd7a8a5dd5a25b9cd53319ad1d620b95fc3267a0))
* capitalization of sensors ([d507162](https://github.com/bj00rn/ha-ferroamp/commit/d5071620b3388dee05e1560aff9a7bd1b4dafe73))
* change link for Mosquitto bridge connections ([bc62cff](https://github.com/bj00rn/ha-ferroamp/commit/bc62cff79d8800f1405f21bc29daaea18c6d980b)), closes [#22](https://github.com/bj00rn/ha-ferroamp/issues/22)
* change usage of deprecated methods ([4d236f8](https://github.com/bj00rn/ha-ferroamp/commit/4d236f8cbbfe0ad5a9ae311327305a4cb98a4ce3))
* commitlint config ([fe9e3fc](https://github.com/bj00rn/ha-ferroamp/commit/fe9e3fcaa3ea50ac8de78e54cc7ba28fd378f87f))
* correct calculation dc link voltage sensor state ([a4a6417](https://github.com/bj00rn/ha-ferroamp/commit/a4a64172c954c4c0c4a365849808e1585ab39da5)), closes [#364](https://github.com/bj00rn/ha-ferroamp/issues/364)
* correct config filename ([aa99106](https://github.com/bj00rn/ha-ferroamp/commit/aa991061fb6642427e266d371d3dd9493ea8b77b))
* **devcontainer:** install pre-commit hooks ([5c5b01d](https://github.com/bj00rn/ha-ferroamp/commit/5c5b01d75fdd64d38990161efbd2def73c9d0c94))
* **docs:** update contribute guidelines ([806c452](https://github.com/bj00rn/ha-ferroamp/commit/806c452c5d9ca826cb35a41fda5ce31dbaef277e))
* don't store events if sensor is not present ([a742062](https://github.com/bj00rn/ha-ferroamp/commit/a742062862c413f362f27e5518ed71e113ccb823))
* enforce codestyle ([9686696](https://github.com/bj00rn/ha-ferroamp/commit/9686696ceb80d7a2f3729b7fe337d930f9471c00))
* failing tests due to blocking calls ([4865308](https://github.com/bj00rn/ha-ferroamp/commit/48653083e89848def1894708f876d96e69a275b9))
* handle asyncio correctly in tests ([a3e2cf8](https://github.com/bj00rn/ha-ferroamp/commit/a3e2cf8d91f5bc514d11d76c64ef672fb8c34a88))
* handle missing values in a better way ([9cea9bf](https://github.com/bj00rn/ha-ferroamp/commit/9cea9bfa65dccccf796a6679ec6d125a5fbaaa32))
* handle new field preview in config in HA 2023.9 ([9456e05](https://github.com/bj00rn/ha-ferroamp/commit/9456e05736cb334a71bd1fa92240b4afd65df42e))
* handle unknown value for energy sensor ([b027287](https://github.com/bj00rn/ha-ferroamp/commit/b0272878396266c78b0b3d747c6cc8ea2e6f9e5b)), closes [#85](https://github.com/bj00rn/ha-ferroamp/issues/85)
* handle unknown value for percentage sensor ([9625906](https://github.com/bj00rn/ha-ferroamp/commit/96259067b69b341292b1f425d9d816f6bc650161)), closes [#162](https://github.com/bj00rn/ha-ferroamp/issues/162)
* ignore context in assertion ([f0b4add](https://github.com/bj00rn/ha-ferroamp/commit/f0b4add9a6b593f541cac635a8745c99105f5778))
* ignore lingering timer tests for now ([1cfefd2](https://github.com/bj00rn/ha-ferroamp/commit/1cfefd2724680ae482bc6555a5c80d6d7b78d903))
* ignore minor_version in config flow test ([c526d96](https://github.com/bj00rn/ha-ferroamp/commit/c526d966ac756c9d18a001c389ae506ae57b5c28))
* ignore unknown last state ([09dcf4a](https://github.com/bj00rn/ha-ferroamp/commit/09dcf4a37163ad86eee75c1e40b10f235c44bc66))
* ignore zero values for total-increasing energy sensors ([e6e0865](https://github.com/bj00rn/ha-ferroamp/commit/e6e0865c41ef5a7db5d25b87ceef6d50203697ed)), closes [#318](https://github.com/bj00rn/ha-ferroamp/issues/318)
* log warn in case of multiple integration entries ([d600559](https://github.com/bj00rn/ha-ferroamp/commit/d600559c74eea9baf2d16c3174a4aa31ef16eb7a))
* make four more sensors total increasing ([f1519f7](https://github.com/bj00rn/ha-ferroamp/commit/f1519f7b950c21ff4690e44f184f9ec019ba6947)), closes [#164](https://github.com/bj00rn/ha-ferroamp/issues/164)
* make relay status history available ([6ceb2f0](https://github.com/bj00rn/ha-ferroamp/commit/6ceb2f07bd1df2b291c750a3d0ff812e7ab2f279)), closes [#92](https://github.com/bj00rn/ha-ferroamp/issues/92)
* make sure old fault codes gets cleared ([5715246](https://github.com/bj00rn/ha-ferroamp/commit/5715246d7f412228ef092e2ea42cfdbbcb13530b))
* mark sensor as added to HASS even if no existing state is found ([1ac896f](https://github.com/bj00rn/ha-ferroamp/commit/1ac896ffc7d594292daf04cf3554bc092b34c8d4))
* only create battery specific sensors if present in message from EnergyHub ([167fbcd](https://github.com/bj00rn/ha-ferroamp/commit/167fbcd1adb5bbdc82f35b4ef30f9fdc828b37f5)), closes [#316](https://github.com/bj00rn/ha-ferroamp/issues/316)
* only migrate ESM entities that actually need migrating ([b77cd6c](https://github.com/bj00rn/ha-ferroamp/commit/b77cd6cc644590e75ecf2eb63ca965eac330c7dc)), closes [#48](https://github.com/bj00rn/ha-ferroamp/issues/48)
* reformat code using pre-commit configuration ([7e2f62b](https://github.com/bj00rn/ha-ferroamp/commit/7e2f62b567dba6cc5c7ede2c63407f37c87fb7eb))
* register version-sensor earlier and actually write state to HA ([3296dee](https://github.com/bj00rn/ha-ferroamp/commit/3296deec8c4c2b6d5d0c01fe50ffc983dddae8f4)), closes [#39](https://github.com/bj00rn/ha-ferroamp/issues/39)
* rename sensors for load balancing ([ddfa4ed](https://github.com/bj00rn/ha-ferroamp/commit/ddfa4ed842695706c1720058c553e98c08d0f3ae)), closes [#66](https://github.com/bj00rn/ha-ferroamp/issues/66)
* replace deprecated constants ([1fd15f5](https://github.com/bj00rn/ha-ferroamp/commit/1fd15f5992a0d241972c6e48ca3026c2e08227ee)), closes [#480](https://github.com/bj00rn/ha-ferroamp/issues/480)
* revert version update from failed release ([37fe28a](https://github.com/bj00rn/ha-ferroamp/commit/37fe28ae192df0ec425ad95429de65dd99068450))
* **sensor:** do not log warning if sensor is not present ([e567226](https://github.com/bj00rn/ha-ferroamp/commit/e567226a7010ac84a15d8bbf4faa8da4319fa45f))
* set native unit of measurement since that seems to be required in HA 2022.4 ([d1fea7f](https://github.com/bj00rn/ha-ferroamp/commit/d1fea7fd9e8ff79ce6c5eb539c816f6fb226bce1))
* strip prefix in non python 3.9+ way ([96a2cbd](https://github.com/bj00rn/ha-ferroamp/commit/96a2cbddd76772dc9417fe6416ce0342e556a1e7))
* support for energy counter being reset ([743cb44](https://github.com/bj00rn/ha-ferroamp/commit/743cb440ed280e5adda2f699f2f2c78d6b819785))
* tests, imports and state-class ([b54b9b1](https://github.com/bj00rn/ha-ferroamp/commit/b54b9b186d93849457756e2673c567c4977e0ebb))
* update branch from main to master in workflow ([3fe52b7](https://github.com/bj00rn/ha-ferroamp/commit/3fe52b71e8e9887ff838486d71c20359bda45a25))
* update fault code attributes keys to strings ([577a1cc](https://github.com/bj00rn/ha-ferroamp/commit/577a1ccae844327bf747609d530844694338db74))
* use async_unload from hass.config_entries ([a2148fb](https://github.com/bj00rn/ha-ferroamp/commit/a2148fba28968e0f572a31949489d72435b62f8b))
* wait for HASS to complete ([6e2f715](https://github.com/bj00rn/ha-ferroamp/commit/6e2f715a4f8277c50bcecb462ac1f174b2244d3d))


### Documentation

* add changelog for releases up to 1.14.2 ([d6e4375](https://github.com/bj00rn/ha-ferroamp/commit/d6e43752f74d7e5aada026ebdb9a956a3edb6125))
* add info on SSO setup ([cb9b7f0](https://github.com/bj00rn/ha-ferroamp/commit/cb9b7f0f289a182ccb428d2af914fa5ae94ee5ec))
* add info regarding battery system ([7b074e9](https://github.com/bj00rn/ha-ferroamp/commit/7b074e9479c6a08911b63f287b6243190e3fc90b))
* adding how to monitor latest version of ferroamp to readme.md ([73bc0ce](https://github.com/bj00rn/ha-ferroamp/commit/73bc0ce8a9717671e79c57de3c64b181346c3f81))
* adding how to monitor latest version of ferroamp to readme.md ([ed6dead](https://github.com/bj00rn/ha-ferroamp/commit/ed6dead76a25158e1beb7c2e2ee6df2a8a150dd0))
* adding how to monitor latest version of ferroamp to readme.md ([1507729](https://github.com/bj00rn/ha-ferroamp/commit/15077293ba2ce9c3b7d9befca48ca8820f64fa5c))
* bugfix on automation to trigger new ferroamp version ([6b347ee](https://github.com/bj00rn/ha-ferroamp/commit/6b347ee64176497d39790d38900a335e77d71488))
* how to setup the Energy Dashboard ([a9e9c2c](https://github.com/bj00rn/ha-ferroamp/commit/a9e9c2c730118b15b399ac9e0cc633f1666534a4))
* increasing scan interval for version scraper in README.md ([63df5e7](https://github.com/bj00rn/ha-ferroamp/commit/63df5e7874f5ae1f9bb97e20b9f917222ed5513e))
* remove not about being work in progress since it's quite stable now ([c77b73d](https://github.com/bj00rn/ha-ferroamp/commit/c77b73d990bf021aa99f47bd93f02035a9ea5f71))


### Miscellaneous Chores

* add contribution info to readme ([99d9902](https://github.com/bj00rn/ha-ferroamp/commit/99d9902d4fef03771fc387b28fe80357a4699d6b))
* add Dependabot config ([b76e853](https://github.com/bj00rn/ha-ferroamp/commit/b76e853fa92df4f50125602dbfa095541752fa93))
* add github actions ([ca2ac01](https://github.com/bj00rn/ha-ferroamp/commit/ca2ac01da3ac23c1f17a7a0afa0df84604f85ab3))
* add HACS-info ([f4ba88c](https://github.com/bj00rn/ha-ferroamp/commit/f4ba88c921a8906353e1aa38a5096f7519b41dc5))
* add info on HACS-installation to readme ([88f1cf9](https://github.com/bj00rn/ha-ferroamp/commit/88f1cf9674ad20b626a322fd776ec41750a25ab0))
* add migration from old to new unique id ([bce9e9c](https://github.com/bj00rn/ha-ferroamp/commit/bce9e9c3ad0a36a265a490ee9a6ed8dd541634fe))
* add name to services ([b5d733a](https://github.com/bj00rn/ha-ferroamp/commit/b5d733a4c14e7fe14de439679418a0f0471a4b63))
* add support for beta-version when releasing from non-master ([a2e11ee](https://github.com/bj00rn/ha-ferroamp/commit/a2e11ee9c04879ffa74e3f1dc69ebc9757af412d))
* add wait option to debug configuration ([17e6fc9](https://github.com/bj00rn/ha-ferroamp/commit/17e6fc992274f05b833a2473caaaf6435dbdbdb3))
* await hass.async_create_task ([612ebae](https://github.com/bj00rn/ha-ferroamp/commit/612ebae491c121330f41a3755f72f9649236f2f9))
* await hass.config_entries.async_forward_entry_setups ([3874c96](https://github.com/bj00rn/ha-ferroamp/commit/3874c9653ab4334396f28e146786f65a2d694b16))
* change exports ([2ae6e26](https://github.com/bj00rn/ha-ferroamp/commit/2ae6e26e6379416a4307d4b1cd4b3d425d84d3b2))
* change Gitter-badge to one that is in the same style as the HACS-badge ([3e3ac6a](https://github.com/bj00rn/ha-ferroamp/commit/3e3ac6aa11c29dc13beafd88e77bcb014ca8f5f8))
* change to new directory structure to prepare for HACS installation ([3446a39](https://github.com/bj00rn/ha-ferroamp/commit/3446a391b2d11ca700c4132651be86c554329877))
* change unit of measurement for ESO and SSO power from kW to W ([564c135](https://github.com/bj00rn/ha-ferroamp/commit/564c135234c1f1ddaccfdbd99a2be570309946da))
* cleanup duplication in tests ([ba0f9d1](https://github.com/bj00rn/ha-ferroamp/commit/ba0f9d1489d276092096513759847e2d561d91ae))
* **devcontainer:** add yaml extension ([8dea8ae](https://github.com/bj00rn/ha-ferroamp/commit/8dea8ae9c812345cff6f6f8f0418d49908f92fd5))
* **devcontainer:** fix pylance not picking up correct interpreter ([d02adc1](https://github.com/bj00rn/ha-ferroamp/commit/d02adc161424740831dc25b678cf07f72958e086))
* **devcontainer:** open HA in browser automatically ([f3022db](https://github.com/bj00rn/ha-ferroamp/commit/f3022dbe8ec9f91992df43d26d3df4c9d8c95990))
* **devcontainer:** remove deprecated settings ([be27046](https://github.com/bj00rn/ha-ferroamp/commit/be270468b47edaa60acff802c101b505433f744c))
* **docs:** add mqtt integration link and fix typo ([4cce8cb](https://github.com/bj00rn/ha-ferroamp/commit/4cce8cb181f1fa32373b8e8b1159c3ec279ebf48))
* fix race condition in postCreateCommand ([36f55a0](https://github.com/bj00rn/ha-ferroamp/commit/36f55a0a9d42404565d93b2fb379cf71cda4e437))
* fix typo ([2d3e3a8](https://github.com/bj00rn/ha-ferroamp/commit/2d3e3a8c0586c33d3d28cf118fcf1be12e6da595))
* **ide:** fix max-line-width for flake8 to same as black and isort ([0192fff](https://github.com/bj00rn/ha-ferroamp/commit/0192fff28868ba27d0b694ce3455d1744849019d))
* **master:** release 1.15.0 ([2fecf02](https://github.com/bj00rn/ha-ferroamp/commit/2fecf021aa8d1de0b57b76338626bb4ed46657d8))
* move and rename constants ([023f07e](https://github.com/bj00rn/ha-ferroamp/commit/023f07ebddfa17529880c533dd6f8075d3316935))
* **pre-commit-hooks:** add commitlint pre-commit hook ([77c2c0d](https://github.com/bj00rn/ha-ferroamp/commit/77c2c0d8df55bd09b7e282c738886452332c971b))
* **pre-commit-hooks:** add some checks, fix requirements files ([11d25fa](https://github.com/bj00rn/ha-ferroamp/commit/11d25fa95b64fa3b1a82c1ca23ec6be250044f54))
* **release:** v0.1.0 ([e57ec7d](https://github.com/bj00rn/ha-ferroamp/commit/e57ec7d5ad901820783f98598463d6202053854a))
* **release:** v0.1.1 ([7519468](https://github.com/bj00rn/ha-ferroamp/commit/751946814a548183efeef86824f291257a2cf366))
* **release:** v1.0.0 ([e7192e9](https://github.com/bj00rn/ha-ferroamp/commit/e7192e969e60acbf164bd32f0a2b6fbd7e1c03cc))
* **release:** v1.1.0 ([83911c8](https://github.com/bj00rn/ha-ferroamp/commit/83911c8c5655a15fb3b1d01e0ab4555f27b91609))
* **release:** v1.10.0 [skip ci] ([2c81af7](https://github.com/bj00rn/ha-ferroamp/commit/2c81af7d5ae1b2c7b7029aa6accbcf02195ab4c4))
* **release:** v1.10.1 [skip ci] ([bcbf2b3](https://github.com/bj00rn/ha-ferroamp/commit/bcbf2b3399f58fa01379a0d4e2c9d248530a63de))
* **release:** v1.10.2 [skip ci] ([0391de4](https://github.com/bj00rn/ha-ferroamp/commit/0391de4696e6bbe40b2ccacd79975e119a2c14d8))
* **release:** v1.11.0 [skip ci] ([d506921](https://github.com/bj00rn/ha-ferroamp/commit/d50692108b3aedef26c1e22ba388f1061b445935))
* **release:** v1.11.1 [skip ci] ([3843a71](https://github.com/bj00rn/ha-ferroamp/commit/3843a714f4560bdafb9777f7dfdea058290df728))
* **release:** v1.11.2 [skip ci] ([3bb7fc1](https://github.com/bj00rn/ha-ferroamp/commit/3bb7fc1fa182fcdcba951065f19ea04efd994d23))
* **release:** v1.12.0 [skip ci] ([79fb34e](https://github.com/bj00rn/ha-ferroamp/commit/79fb34ea005b43724f58f57352445528ec4b80a0))
* **release:** v1.12.1 [skip ci] ([5a2582f](https://github.com/bj00rn/ha-ferroamp/commit/5a2582f67f6b2b24730f3bbc0845cded8c975608))
* **release:** v1.12.2 [skip ci] ([bb77c9a](https://github.com/bj00rn/ha-ferroamp/commit/bb77c9aae9ca401be21416226e143fe8f208b14f))
* **release:** v1.12.3 [skip ci] ([94bf678](https://github.com/bj00rn/ha-ferroamp/commit/94bf678b3ce3ae60f5c03924f835424b122e7a25))
* **release:** v1.12.4 [skip ci] ([56df5e9](https://github.com/bj00rn/ha-ferroamp/commit/56df5e9f542d0b4d9f843acd52ab5107cdcfd614))
* **release:** v1.12.5 [skip ci] ([be9f803](https://github.com/bj00rn/ha-ferroamp/commit/be9f803abc5dd2f39ccb071ed9e90deb0543b4b2))
* **release:** v1.13.0 [skip ci] ([efd0e86](https://github.com/bj00rn/ha-ferroamp/commit/efd0e86989e2ce9b1b90b8430c016460d538bb2a))
* **release:** v1.14.0 [skip ci] ([524df5a](https://github.com/bj00rn/ha-ferroamp/commit/524df5a9b5314d5b91e55304aa2f9954b2cef2cd))
* **release:** v1.14.1 [skip ci] ([e9459d6](https://github.com/bj00rn/ha-ferroamp/commit/e9459d666086a9725c90f32ea3047ca04d1ca483))
* **release:** v1.14.2 [skip ci] ([0e2c305](https://github.com/bj00rn/ha-ferroamp/commit/0e2c3052f1a7e510492b82e73d074cb0896edf27))
* **release:** v1.2.0 ([77fa0c4](https://github.com/bj00rn/ha-ferroamp/commit/77fa0c44aee2430cc5db7290c441323bfef7e1b5))
* **release:** v1.2.1 ([b741052](https://github.com/bj00rn/ha-ferroamp/commit/b741052cd964d417c08995a28135999b4a528104))
* **release:** v1.3.0 ([7745497](https://github.com/bj00rn/ha-ferroamp/commit/7745497273f54aff42bd47700b0214216b050655))
* **release:** v1.4.0 ([810bf71](https://github.com/bj00rn/ha-ferroamp/commit/810bf718ade632667373a121ffe37b6d84cce62a))
* **release:** v1.4.1 ([ffc2c12](https://github.com/bj00rn/ha-ferroamp/commit/ffc2c12e11213a98315eba06a3cd122791d2e226))
* **release:** v1.4.2 ([5aefd37](https://github.com/bj00rn/ha-ferroamp/commit/5aefd37101e44c0421dd3d96af058a70620bd93e))
* **release:** v1.5.0 ([ef598fb](https://github.com/bj00rn/ha-ferroamp/commit/ef598fb6b58cfbe5c3c1175c64fc27f2aaca5170))
* **release:** v1.6.0 ([095ca39](https://github.com/bj00rn/ha-ferroamp/commit/095ca39d15d66b383ea0b425fcb30a6d0dfb8663))
* **release:** v1.7.0 ([18c7132](https://github.com/bj00rn/ha-ferroamp/commit/18c7132bb3d21667105e99de46c84e2a7fe0837d))
* **release:** v1.7.1 ([8c1d310](https://github.com/bj00rn/ha-ferroamp/commit/8c1d310fa87cf5feaa15842e58fa145f0d46c4aa))
* **release:** v1.7.2 ([b037a73](https://github.com/bj00rn/ha-ferroamp/commit/b037a73470882e2dcd5d537a13a8a87f256daa8e))
* **release:** v1.7.3 ([1a44b95](https://github.com/bj00rn/ha-ferroamp/commit/1a44b951a61369eb3148e4a9d9f8d55ebf4a02c8))
* **release:** v1.7.4 [skip ci] ([f5211c9](https://github.com/bj00rn/ha-ferroamp/commit/f5211c9f030e551cbce292c2acb3b5096caba193))
* **release:** v1.7.5 [skip ci] ([0016cb8](https://github.com/bj00rn/ha-ferroamp/commit/0016cb860b62d4a0562c69abb448c03f95de01cc))
* **release:** v1.8.0 [skip ci] ([1f94696](https://github.com/bj00rn/ha-ferroamp/commit/1f9469627ef89022a92b204a1bb7f9b170359e8c))
* **release:** v1.9.0 [skip ci] ([863f847](https://github.com/bj00rn/ha-ferroamp/commit/863f8479272a9c3eb5946c3f5a16ac919d5c5eda))
* **release:** vnull [skip ci] ([ca9a147](https://github.com/bj00rn/ha-ferroamp/commit/ca9a147efafbe87d77c30421e919452e17739216))
* remove dependency on homeassistant ([2aa2f5f](https://github.com/bj00rn/ha-ferroamp/commit/2aa2f5f4646d78cb7b378a804cb4dad74bcf24e7))
* remove logging of phases ([7965730](https://github.com/bj00rn/ha-ferroamp/commit/7965730951041a39a1cf33e80e60f3e037c1ce05))
* remove some duplication ([59056e0](https://github.com/bj00rn/ha-ferroamp/commit/59056e0feeb26d18b5a1511dbcf4331bfad31d79))
* Revert version-update ([45e600c](https://github.com/bj00rn/ha-ferroamp/commit/45e600c1340f1b30f6700ddbd7e016a3a217facc))
* set minimum HA version to 2021.6 ([37e284e](https://github.com/bj00rn/ha-ferroamp/commit/37e284e307339c918c2c05970da076466ff8dc7d))
* sort manifest attributes ([bf10d8f](https://github.com/bj00rn/ha-ferroamp/commit/bf10d8f38d1b4a68c7133814b115a293e01eea85))
* update minimum HA version and bump python to 3.11 ([0d228eb](https://github.com/bj00rn/ha-ferroamp/commit/0d228eb61f8eef9740df2dc8edb4af98c25769ea))
* update README and HACS info ([2420c80](https://github.com/bj00rn/ha-ferroamp/commit/2420c80e1e57c6846b93128e525e5aec413656a4))
* update tests ([511c4d2](https://github.com/bj00rn/ha-ferroamp/commit/511c4d2fcf4868d060a0713c45945bfa1119fc5a))
* update to 3.12 plus some fixes ([f875da9](https://github.com/bj00rn/ha-ferroamp/commit/f875da9160578544076c49a8ffafc0da10987094))
* update to use sensor enums for device and state class ([ddd4418](https://github.com/bj00rn/ha-ferroamp/commit/ddd441897985cbfc84c30ffb8d1efdba6d1d9fdc))
* update version ([9fc61dd](https://github.com/bj00rn/ha-ferroamp/commit/9fc61dd34070ffb1d305391a7b91a2417092ddc8))
* upgrade devcontainer to support 2024.6 ([79e1853](https://github.com/bj00rn/ha-ferroamp/commit/79e1853c5b5e0afd34d5e9209c7a14c5d6380adb))
* use DeviceInfo class ([1d7b276](https://github.com/bj00rn/ha-ferroamp/commit/1d7b276a425e4464a06a74ba2e2e2be0274b0e9f))
* use new enums for energy, power and temperature ([586ff2c](https://github.com/bj00rn/ha-ferroamp/commit/586ff2cd593886a9ef59469415b4278d8f56e45b))
* **vscode:** prompt for remote debug host ([923ae86](https://github.com/bj00rn/ha-ferroamp/commit/923ae86bf917f2547d96393ec6c312678a760012))


### Build System

* **deps-dev:** bump black from 23.10.0 to 23.10.1 ([5fb4af1](https://github.com/bj00rn/ha-ferroamp/commit/5fb4af1a0317aa4a8d0e6d06e57734f800723aae))
* **deps-dev:** bump black from 23.10.1 to 23.11.0 ([7792c5a](https://github.com/bj00rn/ha-ferroamp/commit/7792c5a505df08e23e9f6410671ca0e19ad9d975))
* **deps-dev:** bump black from 23.11.0 to 23.12.0 ([8407836](https://github.com/bj00rn/ha-ferroamp/commit/8407836508fe2b0f58747699c0f53399868b662f))
* **deps-dev:** bump black from 23.12.0 to 23.12.1 ([fd508a5](https://github.com/bj00rn/ha-ferroamp/commit/fd508a542adcb1d5b2510228bd95855f6e7fd55e))
* **deps-dev:** bump black from 23.12.1 to 24.1.1 ([cbf943f](https://github.com/bj00rn/ha-ferroamp/commit/cbf943ff6a26df77b3c44aebc40e5ff8b8005709))
* **deps-dev:** bump black from 23.7.0 to 23.9.1 ([05c143b](https://github.com/bj00rn/ha-ferroamp/commit/05c143be9a4c76f7d1933a2dafd00a5cb5f178ee))
* **deps-dev:** bump black from 23.9.1 to 23.10.0 ([dc9b4e4](https://github.com/bj00rn/ha-ferroamp/commit/dc9b4e4f94fe273509b361829deca7aec5c2169d))
* **deps-dev:** bump black from 24.1.1 to 24.2.0 ([47737a6](https://github.com/bj00rn/ha-ferroamp/commit/47737a6ca2b2d56d0ef50f6ddaf207f155b0bd2d))
* **deps-dev:** bump black from 24.2.0 to 24.3.0 ([3b1edd0](https://github.com/bj00rn/ha-ferroamp/commit/3b1edd048b4bcc60745f5c14359503ca4ef55366))
* **deps-dev:** bump black from 24.3.0 to 24.4.0 ([154ce7f](https://github.com/bj00rn/ha-ferroamp/commit/154ce7f77ddd79610c2d6c0f84698e96c027d554))
* **deps-dev:** bump black from 24.4.0 to 24.4.1 ([f5e5b97](https://github.com/bj00rn/ha-ferroamp/commit/f5e5b97bdc4f8c35ac967472ad265c88fca41920))
* **deps-dev:** bump black from 24.4.1 to 24.4.2 ([3633930](https://github.com/bj00rn/ha-ferroamp/commit/3633930ec9e8b0833afe4945cd9ba3fc07859875))
* **deps-dev:** bump black from 24.4.2 to 24.8.0 ([8486f13](https://github.com/bj00rn/ha-ferroamp/commit/8486f1325c6d4f55f43ec0cbfae308955dc22c81))
* **deps-dev:** bump black from 24.8.0 to 24.10.0 ([4a2f7dd](https://github.com/bj00rn/ha-ferroamp/commit/4a2f7ddf5c42f8f007e55304047530e2308f19e8))
* **deps-dev:** bump flake8 from 6.0.0 to 6.1.0 ([a090fb6](https://github.com/bj00rn/ha-ferroamp/commit/a090fb673184afd5f43bff97ac2c89c64fb51f2e))
* **deps-dev:** bump flake8 from 6.1.0 to 7.0.0 ([c8579b1](https://github.com/bj00rn/ha-ferroamp/commit/c8579b15b3ad2b4c4c8eecbea06d15ede544d337))
* **deps-dev:** bump flake8 from 7.0.0 to 7.1.0 ([93336ee](https://github.com/bj00rn/ha-ferroamp/commit/93336eed77a4a6b3d2afe36b0c8e3ecc134124bd))
* **deps-dev:** bump flake8 from 7.1.0 to 7.1.1 ([152596b](https://github.com/bj00rn/ha-ferroamp/commit/152596b2139bb9b192a2a106c3de67aa968102a9))
* **deps-dev:** bump isort from 5.12.0 to 5.13.0 ([53625f5](https://github.com/bj00rn/ha-ferroamp/commit/53625f516d214c137fc44c25e824fba9bcd79a95))
* **deps-dev:** bump isort from 5.13.0 to 5.13.1 ([37c9cbc](https://github.com/bj00rn/ha-ferroamp/commit/37c9cbcf1256c9755d48fa073053fe308e985e12))
* **deps-dev:** bump isort from 5.13.1 to 5.13.2 ([b46630f](https://github.com/bj00rn/ha-ferroamp/commit/b46630fb869b44e13be54f0e9871a30c56f843cb))
* **deps-dev:** bump pre-commit from 3.3.3 to 3.4.0 ([c4677d8](https://github.com/bj00rn/ha-ferroamp/commit/c4677d8a36d3b4324c081e0cdc326284bd531d06))
* **deps-dev:** bump pre-commit from 3.4.0 to 3.5.0 ([910787a](https://github.com/bj00rn/ha-ferroamp/commit/910787ab81cccdb6f590414cce83113aa829a6bd))
* **deps-dev:** bump pre-commit from 3.5.0 to 3.6.0 ([17c7c3f](https://github.com/bj00rn/ha-ferroamp/commit/17c7c3f330e0c88048b2cb4312619e558e879117))
* **deps-dev:** bump pre-commit from 3.6.0 to 3.6.1 ([72ea099](https://github.com/bj00rn/ha-ferroamp/commit/72ea0993052644ed4c589f0264d9734695173016))
* **deps-dev:** bump pre-commit from 3.6.1 to 3.6.2 ([5510613](https://github.com/bj00rn/ha-ferroamp/commit/5510613b14227239a3ab3b3b871374858de1535d))
* **deps-dev:** bump pre-commit from 3.6.2 to 3.7.0 ([9d7936f](https://github.com/bj00rn/ha-ferroamp/commit/9d7936fb94b57f786f5b35962d53778a1e0f546c))
* **deps-dev:** bump pre-commit from 3.7.0 to 3.7.1 ([9b752a8](https://github.com/bj00rn/ha-ferroamp/commit/9b752a8303436e543bf733446b01d406290ca52c))
* **deps-dev:** bump pre-commit from 3.7.1 to 3.8.0 ([6adcf5a](https://github.com/bj00rn/ha-ferroamp/commit/6adcf5ad83e8ca6500ca9c60f073c55f3eb931b6))
* **deps-dev:** bump pre-commit from 3.8.0 to 4.0.0 ([adae2e9](https://github.com/bj00rn/ha-ferroamp/commit/adae2e97a5a436a99128e6c90e5fdd573233eb16))
* **deps-dev:** bump pre-commit from 4.0.0 to 4.0.1 ([45aef48](https://github.com/bj00rn/ha-ferroamp/commit/45aef4887434c47b671097a8d8a2cfd516e25285))
* **deps:** bump actions/checkout from 2 to 3 ([a5bc15b](https://github.com/bj00rn/ha-ferroamp/commit/a5bc15bb52c49734a37b7d3d58bf88ad7f48c73d))
* **deps:** bump actions/checkout from 3 to 4 ([ca50a50](https://github.com/bj00rn/ha-ferroamp/commit/ca50a500ae2b2d79a6080507061e263beb400236))
* **deps:** bump actions/setup-node from 2 to 3 ([f982a29](https://github.com/bj00rn/ha-ferroamp/commit/f982a2904235e669c8b872e6faaa18d98a0e5f47))
* **deps:** bump actions/setup-python from 2 to 3.1.0 ([c7ed4e4](https://github.com/bj00rn/ha-ferroamp/commit/c7ed4e429cb7d56e9e7111ad9e2f9b9867d55bb9))
* **deps:** bump actions/setup-python from 3 to 4 ([5a0d40a](https://github.com/bj00rn/ha-ferroamp/commit/5a0d40a2aa24a388293e3c9fa81905cf14a9efd4))
* **deps:** bump actions/setup-python from 3.1.0 to 3.1.1 ([a10a155](https://github.com/bj00rn/ha-ferroamp/commit/a10a155ff33b4e441bed0166c733e8bb2d77cf27))
* **deps:** bump actions/setup-python from 3.1.1 to 3.1.2 ([71444fb](https://github.com/bj00rn/ha-ferroamp/commit/71444fb8b8733c053f752eba8ea20c24d600a9fc))
* **deps:** bump actions/setup-python from 3.1.2 to 4.0.0 ([0f270ac](https://github.com/bj00rn/ha-ferroamp/commit/0f270acaf472031cf8b179c5db9929ce1c2a83ca))
* **deps:** bump actions/setup-python from 4 to 5 ([5569de5](https://github.com/bj00rn/ha-ferroamp/commit/5569de5bf7838e75d786d97c54abe0257dbf05ad))
* **deps:** bump actions/setup-python from 4.0.0 to 4.1.0 ([ac15ac3](https://github.com/bj00rn/ha-ferroamp/commit/ac15ac3995a54102ac13bfbe3aa97156f26df71e))
* **deps:** bump actions/setup-python from 4.1.0 to 4.2.0 ([a4a0331](https://github.com/bj00rn/ha-ferroamp/commit/a4a0331beeedef0c0897ba1befe5a0241d40bc30))
* **deps:** bump actions/setup-python from 4.2.0 to 4.3.0 ([fa7b001](https://github.com/bj00rn/ha-ferroamp/commit/fa7b00163a7454c2fc6fee4e2ad63444bd7d2233))
* **deps:** bump actions/setup-python from 4.3.0 to 4.3.1 ([057f4d1](https://github.com/bj00rn/ha-ferroamp/commit/057f4d1ab5857dfc03300b409afd20baee3e419e))
* **deps:** bump actions/setup-python from 4.3.1 to 4.4.0 ([8644e5f](https://github.com/bj00rn/ha-ferroamp/commit/8644e5f1254d7358622b04edefc0c0434beff861))
* **deps:** bump actions/setup-python from 4.4.0 to 4.5.0 ([39dd67d](https://github.com/bj00rn/ha-ferroamp/commit/39dd67d55462b5b91ad1b931f8b9f7048a6fc484))
* **deps:** bump actions/setup-python from 4.5.0 to 4.6.0 ([d4c4f0a](https://github.com/bj00rn/ha-ferroamp/commit/d4c4f0a20206fc8e8954174d0a14339de6a40dad))
* **deps:** bump actions/setup-python from 4.6.0 to 4.6.1 ([a828470](https://github.com/bj00rn/ha-ferroamp/commit/a828470878690364722fb035bf568e93a3f4b3b6))
* **deps:** bump actions/setup-python from 4.6.1 to 4.7.0 ([d7d215c](https://github.com/bj00rn/ha-ferroamp/commit/d7d215c10b5ef2d96296908181f509803ef58d78))
* **deps:** bump github/codeql-action from 1 to 2 ([d8541fa](https://github.com/bj00rn/ha-ferroamp/commit/d8541fa7d8c0afa38e6d8edad05def09dd183f2e))
* **deps:** bump github/codeql-action from 2 to 3 ([8380f1e](https://github.com/bj00rn/ha-ferroamp/commit/8380f1eb0e885c9a655ba6ff01279c4b2f852983))
* **deps:** bump janus from 1.0.0 to 1.1.0 ([bcdd5c5](https://github.com/bj00rn/ha-ferroamp/commit/bcdd5c5b5f985d21015d45c4d2324da4c02f86d8))
* **deps:** bump paho-mqtt from 1.5.1 to 1.6.0 ([b3524bd](https://github.com/bj00rn/ha-ferroamp/commit/b3524bd41b04c5b2503f6a666abfce215c37686c))
* **deps:** bump paho-mqtt from 1.6.0 to 1.6.1 ([2942b68](https://github.com/bj00rn/ha-ferroamp/commit/2942b68dc73ec7260f668c4b0f897f920c4a6aba))
* **deps:** bump pre-commit/action from 3.0.0 to 3.0.1 ([db9c537](https://github.com/bj00rn/ha-ferroamp/commit/db9c537087788ed4843696e894c75591648f9dfe))
* **deps:** bump pytest-homeassistant-custom-component ([03add58](https://github.com/bj00rn/ha-ferroamp/commit/03add5875faa80004aa3914c8e7dbdcce85b5872))
* **deps:** bump pytest-homeassistant-custom-component ([acb4647](https://github.com/bj00rn/ha-ferroamp/commit/acb46470707fd7761972f6e8f17d8e6c56126cf9))
* **deps:** bump pytest-homeassistant-custom-component ([3af1ab8](https://github.com/bj00rn/ha-ferroamp/commit/3af1ab82997f6e3272b04cb14af47070cfac025c))
* **deps:** bump pytest-homeassistant-custom-component ([1e10c9c](https://github.com/bj00rn/ha-ferroamp/commit/1e10c9c54b162c9be39d4527f5211c234db94ffd))
* **deps:** bump pytest-homeassistant-custom-component ([3d6fbd9](https://github.com/bj00rn/ha-ferroamp/commit/3d6fbd9ca9c1874f1db96949f40147fae73b787f))
* **deps:** bump pytest-homeassistant-custom-component ([a57f102](https://github.com/bj00rn/ha-ferroamp/commit/a57f10253b49862f69833b7eb626c1b00dbf0ba6))
* **deps:** bump pytest-homeassistant-custom-component ([2067900](https://github.com/bj00rn/ha-ferroamp/commit/2067900961dfed15aa80c095c03241fbda61488d))
* **deps:** bump pytest-homeassistant-custom-component ([5952f35](https://github.com/bj00rn/ha-ferroamp/commit/5952f3516bd871ea4caa3b6560a3c641d4f371fe))
* **deps:** bump pytest-homeassistant-custom-component ([1466725](https://github.com/bj00rn/ha-ferroamp/commit/1466725bc776f171e5a527edbb44d70b5ff809d6))
* **deps:** bump TriPSs/conventional-changelog-action from 3 to 4 ([5539270](https://github.com/bj00rn/ha-ferroamp/commit/55392706018ceb55e1163188da75145022b19cc8))
* **deps:** bump TriPSs/conventional-changelog-action from 4 to 5 ([37d5e60](https://github.com/bj00rn/ha-ferroamp/commit/37d5e6045f6505e773d41cd1edd7306140bf8e60))
* **deps:** bump wagoid/commitlint-github-action from 4 to 5 ([cefa870](https://github.com/bj00rn/ha-ferroamp/commit/cefa870173b9c802b25950e939f1906399b10163))
* **deps:** bump wagoid/commitlint-github-action from 5 to 6 ([297bdca](https://github.com/bj00rn/ha-ferroamp/commit/297bdcaaf7c558d56445782a259575c19deaae84))
* remove direct dependency on voluptous ([8eab242](https://github.com/bj00rn/ha-ferroamp/commit/8eab2421429c3d5759355ed02db73a9e0278bb18))
* use released version of pytest-homeassistant-custom-component ([ac10c10](https://github.com/bj00rn/ha-ferroamp/commit/ac10c10790edca9f92c3951bee8f4999a57ff665))


### Continuous Integration

* add commitlint action ([25f3072](https://github.com/bj00rn/ha-ferroamp/commit/25f307216ec643f455edea41d5dad399435c8994))
* add config for commitlint ([c6a7cca](https://github.com/bj00rn/ha-ferroamp/commit/c6a7ccaf7030373de1cc0797e1c489333c01b932))
* add conventional changelog configuration ([f1ef076](https://github.com/bj00rn/ha-ferroamp/commit/f1ef076e2a2e3355c58ac6c92677a3065d478045))
* add minimal package.json to get commitlint to run correctly ([d1b1c71](https://github.com/bj00rn/ha-ferroamp/commit/d1b1c711dfc8ad21e168a5c71722a5889f4116d7))
* add python 3.10 to package workflow ([0cffc18](https://github.com/bj00rn/ha-ferroamp/commit/0cffc18ac73fce52d2732e7fa9b6e97d172a1a7c))
* add python 3.11 to test matrix ([8e460e3](https://github.com/bj00rn/ha-ferroamp/commit/8e460e35375cfda3571078460ef8ec31bf101afe))
* allow longer body-lines for all commits and remove node-dependency ([61278ac](https://github.com/bj00rn/ha-ferroamp/commit/61278ac93f4bce366a42026a46b89f111cb1e34b))
* drop support for Python 3.9 since HA no longer supports it ([8e1600e](https://github.com/bj00rn/ha-ferroamp/commit/8e1600e777505ce7ed0caec2111b44ae35b1249e))
* migrate to release-please flow ([7583cf1](https://github.com/bj00rn/ha-ferroamp/commit/7583cf15c76202a78f547e034ce73cf753c65fc4))
* remove python 3.11 from test matrix since not supported by HA yet ([8d3151c](https://github.com/bj00rn/ha-ferroamp/commit/8d3151cd8a187d9135a31d7e24d98ec53a0b4de5))
* replace deprecated release action ([8281c0f](https://github.com/bj00rn/ha-ferroamp/commit/8281c0f55b700351e1f1617d4aef56381d7d6292))
* run build and test on PRs ([ea82a4b](https://github.com/bj00rn/ha-ferroamp/commit/ea82a4b5a84ac6c3196af3a5eb80ae5fe86839ea))
* set Python version in pre-commit GitHub workflow ([ef63777](https://github.com/bj00rn/ha-ferroamp/commit/ef63777ff2e6aa7f5fcdc02c2e3418c5819ee87e))
* update config to extend config-conventional ([2d2ab44](https://github.com/bj00rn/ha-ferroamp/commit/2d2ab44e4fd002db9c1f667047e96f270e9efffe))

## [1.15.0](https://github.com/henricm/ha-ferroamp/compare/v1.14.2...v1.15.0) (2024-10-25)


### Features

* **changelog:** add custom sections for changelog types ([35112a4](https://github.com/henricm/ha-ferroamp/commit/35112a4d613bb753c7abbbd830cc8b22d32e2e3f))


### Bug Fixes

* correct config filename ([aa99106](https://github.com/henricm/ha-ferroamp/commit/aa991061fb6642427e266d371d3dd9493ea8b77b))
* revert version update from failed release ([37fe28a](https://github.com/henricm/ha-ferroamp/commit/37fe28ae192df0ec425ad95429de65dd99068450))
* update branch from main to master in workflow ([3fe52b7](https://github.com/henricm/ha-ferroamp/commit/3fe52b71e8e9887ff838486d71c20359bda45a25))


### Documentation

* add changelog for releases up to 1.14.2 ([d6e4375](https://github.com/henricm/ha-ferroamp/commit/d6e43752f74d7e5aada026ebdb9a956a3edb6125))


### Miscellaneous Chores

* await hass.config_entries.async_forward_entry_setups ([3874c96](https://github.com/henricm/ha-ferroamp/commit/3874c9653ab4334396f28e146786f65a2d694b16))
* **release:** vnull [skip ci] ([ca9a147](https://github.com/henricm/ha-ferroamp/commit/ca9a147efafbe87d77c30421e919452e17739216))


### Build System

* **deps-dev:** bump black from 24.4.2 to 24.8.0 ([8486f13](https://github.com/henricm/ha-ferroamp/commit/8486f1325c6d4f55f43ec0cbfae308955dc22c81))
* **deps-dev:** bump black from 24.8.0 to 24.10.0 ([4a2f7dd](https://github.com/henricm/ha-ferroamp/commit/4a2f7ddf5c42f8f007e55304047530e2308f19e8))
* **deps-dev:** bump flake8 from 7.1.0 to 7.1.1 ([152596b](https://github.com/henricm/ha-ferroamp/commit/152596b2139bb9b192a2a106c3de67aa968102a9))
* **deps-dev:** bump pre-commit from 3.7.1 to 3.8.0 ([6adcf5a](https://github.com/henricm/ha-ferroamp/commit/6adcf5ad83e8ca6500ca9c60f073c55f3eb931b6))
* **deps-dev:** bump pre-commit from 3.8.0 to 4.0.0 ([adae2e9](https://github.com/henricm/ha-ferroamp/commit/adae2e97a5a436a99128e6c90e5fdd573233eb16))
* **deps-dev:** bump pre-commit from 4.0.0 to 4.0.1 ([45aef48](https://github.com/henricm/ha-ferroamp/commit/45aef4887434c47b671097a8d8a2cfd516e25285))


### Continuous Integration

* add conventional changelog configuration ([f1ef076](https://github.com/henricm/ha-ferroamp/commit/f1ef076e2a2e3355c58ac6c92677a3065d478045))
* migrate to release-please flow ([7583cf1](https://github.com/henricm/ha-ferroamp/commit/7583cf15c76202a78f547e034ce73cf753c65fc4))
* set Python version in pre-commit GitHub workflow ([ef63777](https://github.com/henricm/ha-ferroamp/commit/ef63777ff2e6aa7f5fcdc02c2e3418c5819ee87e))

## [1.14.2] - 2024-07-03

### Bug Fixes

- Commitlint config
- Use async_unload from hass.config_entries
- Add wait_background_tasks parameter to block_till_done function
- Ignore lingering timer tests for now
- Update fault code attributes keys to strings
- Replace deprecated constants

### Miscellaneous Tasks

- Update to 3.12 plus some fixes
- Await hass.async_create_task
- *(release)* V1.14.2 [skip ci]

### Build

- *(deps-dev)* Bump black from 23.12.1 to 24.1.1
- *(deps)* Bump pre-commit/action from 3.0.0 to 3.0.1
- *(deps-dev)* Bump pre-commit from 3.6.0 to 3.6.1
- *(deps-dev)* Bump black from 24.1.1 to 24.2.0
- *(deps-dev)* Bump pre-commit from 3.6.1 to 3.6.2
- *(deps-dev)* Bump black from 24.2.0 to 24.3.0
- *(deps-dev)* Bump pre-commit from 3.6.2 to 3.7.0
- *(deps)* Bump wagoid/commitlint-github-action from 5 to 6
- *(deps-dev)* Bump black from 24.3.0 to 24.4.0
- *(deps-dev)* Bump black from 24.4.0 to 24.4.1
- *(deps-dev)* Bump black from 24.4.1 to 24.4.2
- *(deps-dev)* Bump pre-commit from 3.7.0 to 3.7.1
- *(deps)* Bump pytest-homeassistant-custom-component
- *(deps-dev)* Bump flake8 from 7.0.0 to 7.1.0

## [1.14.1] - 2024-01-17

### Bug Fixes

- Add name to service fields
- Handle new field preview in config in HA 2023.9
- Ignore minor_version in config flow test
- *(sensor)* Do not log warning if sensor is not present

### Miscellaneous Tasks

- *(pre-commit-hooks)* Add some checks, fix requirements files
- *(devcontainer)* Remove deprecated settings
- *(devcontainer)* Add yaml extension
- *(devcontainer)* Fix pylance not picking up correct interpreter
- *(pre-commit-hooks)* Add commitlint pre-commit hook
- *(ide)* Fix max-line-width for flake8 to same as black and isort
- *(devcontainer)* Open HA in browser automatically
- *(docs)* Add mqtt integration link and fix typo
- Fix race condition in postCreateCommand
- Add wait option to debug configuration
- *(vscode)* Prompt for remote debug host
- *(release)* V1.14.1 [skip ci]

### Build

- *(deps-dev)* Bump pre-commit from 3.3.3 to 3.4.0
- *(deps)* Bump actions/checkout from 3 to 4
- *(deps-dev)* Bump black from 23.7.0 to 23.9.1
- *(deps-dev)* Bump pre-commit from 3.4.0 to 3.5.0
- *(deps-dev)* Bump black from 23.9.1 to 23.10.0
- *(deps-dev)* Bump black from 23.10.0 to 23.10.1
- *(deps-dev)* Bump black from 23.10.1 to 23.11.0
- *(deps)* Bump actions/setup-python from 4 to 5
- *(deps-dev)* Bump isort from 5.12.0 to 5.13.0
- *(deps-dev)* Bump pre-commit from 3.5.0 to 3.6.0
- *(deps-dev)* Bump isort from 5.13.0 to 5.13.1
- *(deps-dev)* Bump black from 23.11.0 to 23.12.0
- *(deps-dev)* Bump isort from 5.13.1 to 5.13.2
- *(deps)* Bump github/codeql-action from 2 to 3
- *(deps-dev)* Bump black from 23.12.0 to 23.12.1
- *(deps)* Bump TriPSs/conventional-changelog-action from 4 to 5
- *(deps-dev)* Bump flake8 from 6.1.0 to 7.0.0

## [1.14.0] - 2023-08-17

### Features

- Vscode devcontainer configuration
- *(ci)* Add github action to run pre-commit
- Remove precision config since now builtin to HA

### Bug Fixes

- Enforce codestyle
- Reformat code using pre-commit configuration
- *(devcontainer)* Install pre-commit hooks
- *(docs)* Update contribute guidelines

### Miscellaneous Tasks

- Add name to services
- Update minimum HA version and bump python to 3.11
- *(release)* V1.14.0 [skip ci]

### Build

- *(deps-dev)* Bump flake8 from 6.0.0 to 6.1.0
- *(deps)* Bump actions/setup-python from 3 to 4
- *(deps)* Bump TriPSs/conventional-changelog-action from 3 to 4

## [1.13.0] - 2023-07-26

### Features

- Add separate entities per phase

### Bug Fixes

- Capitalization of sensors

### Miscellaneous Tasks

- *(release)* V1.13.0 [skip ci]

### Build

- *(deps)* Bump actions/setup-python from 4.6.1 to 4.7.0

## [1.12.5] - 2023-07-08

### Bug Fixes

- Correct calculation dc link voltage sensor state

### Miscellaneous Tasks

- *(release)* V1.12.5 [skip ci]

## [1.12.4] - 2023-07-07

### Bug Fixes

- Add additional SSO fault codes

### Documentation

- Adding how to monitor latest version of ferroamp to readme.md
- Adding how to monitor latest version of ferroamp to readme.md
- Adding how to monitor latest version of ferroamp to readme.md
- Increasing scan interval for version scraper in README.md
- Bugfix on automation to trigger new ferroamp version

### Miscellaneous Tasks

- *(release)* V1.12.4 [skip ci]

### Build

- *(deps)* Bump actions/setup-python from 4.6.0 to 4.6.1

## [1.12.3] - 2023-05-02

### Bug Fixes

- Ignore unknown last state

### Miscellaneous Tasks

- *(release)* V1.12.3 [skip ci]

## [1.12.2] - 2023-04-24

### Bug Fixes

- Only create battery specific sensors if present in message from EnergyHub

### Miscellaneous Tasks

- *(release)* V1.12.2 [skip ci]

### Build

- *(deps)* Bump actions/setup-python from 4.5.0 to 4.6.0

## [1.12.1] - 2023-04-15

### Bug Fixes

- Add control status sensor on init

### Miscellaneous Tasks

- *(release)* V1.12.1 [skip ci]

## [1.12.0] - 2023-04-05

### Features

- Added possibility to turn on debug logging of events

### Miscellaneous Tasks

- *(release)* V1.12.0 [skip ci]

## [1.11.2] - 2023-04-05

### Bug Fixes

- Wait for HASS to complete
- Don't store events if sensor is not present
- Ignore zero values for total-increasing energy sensors

### Miscellaneous Tasks

- *(release)* V1.11.2 [skip ci]

## [1.11.1] - 2023-03-21

### Bug Fixes

- Make sure old fault codes gets cleared

### Miscellaneous Tasks

- *(release)* V1.11.1 [skip ci]

## [1.11.0] - 2023-03-18

### Features

- Only add sensors for loadbalancing if present in message

### Miscellaneous Tasks

- Update config to extend config-conventional
- Add contribution info to readme
- *(release)* V1.11.0 [skip ci]

## [1.10.2] - 2023-03-09

### Bug Fixes

- Support for energy counter being reset

### Miscellaneous Tasks

- Add python 3.11 to test matrix
- Remove python 3.11 from test matrix since not supported by HA yet
- Drop support for Python 3.9 since HA no longer supports it
- Replace deprecated release action
- Sort manifest attributes
- *(release)* V1.10.2 [skip ci]

### Build

- *(deps)* Bump actions/setup-python from 4.3.1 to 4.4.0
- *(deps)* Bump actions/setup-python from 4.4.0 to 4.5.0

## [1.10.1] - 2022-12-19

### Bug Fixes

- Log warn in case of multiple integration entries

### Miscellaneous Tasks

- Run build and test on PRs
- *(release)* V1.10.1 [skip ci]

## [1.10.0] - 2022-12-12

### Features

- Updating readme.md
- Make sure MQTT integration is loaded before setup

### Bug Fixes

- Ignore context in assertion
- Handle asyncio correctly in tests

### Miscellaneous Tasks

- Allow longer body-lines for all commits and remove node-dependency
- Use new enums for energy, power and temperature
- *(release)* V1.10.0 [skip ci]

### Build

- *(deps)* Bump actions/setup-python from 4.2.0 to 4.3.0
- *(deps)* Bump actions/setup-python from 4.3.0 to 4.3.1
- *(deps)* Bump pytest-homeassistant-custom-component

## [1.9.0] - 2022-08-09

### Features

- Requirements for hacs default
- Change name for hacs.yaml

### Miscellaneous Tasks

- *(release)* V1.9.0 [skip ci]

## [1.8.0] - 2022-08-08

### Features

- Migrate to new entity naming style

### Miscellaneous Tasks

- *(release)* V1.8.0 [skip ci]

### Build

- *(deps)* Bump actions/setup-python from 4.1.0 to 4.2.0

## [1.7.5] - 2022-07-25

### Bug Fixes

- Battery icon not shown when below 10 percent

### Miscellaneous Tasks

- Add minimal package.json to get commitlint to run correctly
- Add python 3.10 to package workflow
- *(release)* V1.7.5 [skip ci]

### Build

- *(deps)* Bump actions/setup-python from 3.1.2 to 4.0.0
- *(deps)* Bump wagoid/commitlint-github-action from 4 to 5
- *(deps)* Bump actions/setup-node from 2 to 3
- *(deps)* Bump actions/setup-python from 4.0.0 to 4.1.0

## [1.7.4] - 2022-06-02

### Bug Fixes

- Change usage of deprecated methods

### Miscellaneous Tasks

- *(release)* V1.7.4 [skip ci]

### Build

- *(deps)* Bump pytest-homeassistant-custom-component

## [1.7.3] - 2022-05-04

### Bug Fixes

- Handle unknown value for percentage sensor
- Make four more sensors total increasing

### Miscellaneous Tasks

- *(release)* V1.7.3

### Build

- *(deps)* Bump actions/setup-python from 3.1.0 to 3.1.1
- *(deps)* Bump actions/setup-python from 3.1.1 to 3.1.2
- *(deps)* Bump github/codeql-action from 1 to 2

## [1.7.2] - 2022-04-05

### Bug Fixes

- Set native unit of measurement since that seems to be required in HA 2022.4

### Miscellaneous Tasks

- *(release)* V1.7.2

### Build

- *(deps)* Bump actions/setup-python from 2 to 3.1.0
- *(deps)* Bump pytest-homeassistant-custom-component

## [1.7.1] - 2022-03-17

### Bug Fixes

- Mark sensor as added to HASS even if no existing state is found

### Miscellaneous Tasks

- *(release)* V1.7.1

### Build

- *(deps)* Bump actions/checkout from 2 to 3
- *(deps)* Bump pytest-homeassistant-custom-component

## [1.7.0] - 2022-02-21

### Features

- Make sure that 3-phase energy sensors are strictly increasing

### Bug Fixes

- Failing tests due to blocking calls

### Miscellaneous Tasks

- Update to use sensor enums for device and state class
- *(release)* V1.7.0

### Build

- *(deps)* Bump pytest-homeassistant-custom-component

## [1.6.0] - 2021-12-08

### Features

- Updated to support Home Assistant 2021.12

### Miscellaneous Tasks

- *(release)* V1.6.0

### Build

- *(deps)* Bump pytest-homeassistant-custom-component

## [1.5.0] - 2021-12-04

### Features

- Add sensor for load balancing

### Miscellaneous Tasks

- *(release)* V1.5.0

## [1.4.2] - 2021-11-21

### Bug Fixes

- Make relay status history available

### Miscellaneous Tasks

- Add config for commitlint
- *(release)* V1.4.2

## [1.4.1] - 2021-11-05

### Bug Fixes

- Handle unknown value for energy sensor

### Miscellaneous Tasks

- Use DeviceInfo class
- *(release)* V1.4.1

### Build

- *(deps)* Bump pytest-homeassistant-custom-component
- *(deps)* Bump paho-mqtt from 1.5.1 to 1.6.0
- *(deps)* Bump paho-mqtt from 1.6.0 to 1.6.1
- *(deps)* Bump pytest-homeassistant-custom-component

## [1.4.0] - 2021-09-27

### Features

- Make sure state is always increasing for energy sensors

### Bug Fixes

- Handle missing values in a better way
- Average calculation

### Documentation

- How to setup the Energy Dashboard
- Add info on SSO setup
- Add info regarding battery system

### Miscellaneous Tasks

- *(release)* V1.4.0

### Build

- Use released version of pytest-homeassistant-custom-component
- Remove direct dependency on voluptous

## [1.3.0] - 2021-09-01

### Features

- Updated to support Home Assistant 2021.9 long term stats
- Add support for long-term statistics to SSO energy sensor

### Miscellaneous Tasks

- *(release)* V1.3.0

## [1.2.1] - 2021-08-28

### Bug Fixes

- Rename sensors for load balancing

### Miscellaneous Tasks

- Add Dependabot config
- Add commitlint action
- Remove dependency on homeassistant
- *(release)* V1.2.1

## [1.2.0] - 2021-08-09

### Features

- Add last_reset to battery energy sensors
- Remove integration name from sensor names

### Miscellaneous Tasks

- Update tests
- *(release)* V1.2.0

## [1.1.0] - 2021-08-05

### Features

- Add sensors used for load balancing applications.

### Bug Fixes

- Tests, imports and state-class

### Documentation

- Remove not about being work in progress since it's quite stable now

### Miscellaneous Tasks

- Update version
- *(release)* V1.1.0

## [1.0.0] - 2021-08-04

### Miscellaneous Tasks

- Revert version-update

## [1.0.0-beta] - 2021-08-03

### Features

- [**breaking**] Add support for Home Assistant Home Energy Management

### Miscellaneous Tasks

- Add support for beta-version when releasing from non-master
- Change exports
- *(release)* V1.0.0

## [0.1.1] - 2021-08-03

### Bug Fixes

- Only migrate ESM entities that actually need migrating

### Miscellaneous Tasks

- *(release)* V0.1.1

## [0.1.0] - 2021-07-27

### Features

- Update to HA 2021.7 and use entity attrs
- Add release workflow

### Miscellaneous Tasks

- Cleanup duplication in tests
- Move and rename constants
- Remove some duplication
- Set minimum HA version to 2021.6
- *(release)* V0.1.0

## [0.0.6] - 2021-07-08

### Features

- Trim ESM name to just serial number
- Add textual representation of ESO faultcodes as attributes
- Add SSO fault codes

### Bug Fixes

- Register version-sensor earlier and actually write state to HA

### Miscellaneous Tasks

- Remove logging of phases

## [0.0.5] - 2021-07-06

### Features

- Add missing ESM Rated Power sensor
- Add sensor for extapi version
- Remove model-info from SSO-name

### Bug Fixes

- Strip prefix in non python 3.9+ way

### Miscellaneous Tasks

- Add migration from old to new unique id
- Change Gitter-badge to one that is in the same style as the HACS-badge

## [0.0.4] - 2021-06-27

### Features

- Add missing sensor for Adaptive Current Equalization
- Add sensor for estimated grid frequency
- Change default precisions and make them configurable
- Add option for frequency precision
- Add ESM status sensor
- Add sensor for last command and status

### Bug Fixes

- Change link for Mosquitto bridge connections

### Miscellaneous Tasks

- Change unit of measurement for ESO and SSO power from kW to W
- Fix typo

## [0.0.3-beta] - 2021-05-24

### Features

- Add selectors to services and add tests

### Miscellaneous Tasks

- Add info on HACS-installation to readme
- Update README and HACS info

## [0.0.2] - 2021-05-24

### Miscellaneous Tasks

- Add github actions
- Add HACS-info

## [0.0.1] - 2021-05-20

### Features

- Add config and option flow, multiple hubs

### Miscellaneous Tasks

- Change to new directory structure to prepare for HACS installation

<!-- generated by git-cliff -->
