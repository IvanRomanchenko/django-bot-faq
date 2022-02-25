import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="django-bot-faq",
	version="0.1.2",
	author="Ivan Romanchenko",
	author_email="vanvanych789@gmail.com",
	description="FAQ module",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/IvanRomanchenko/django-bot-faq",
	packages=["bot_faq", ],
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3.10",
		"Framework :: Django :: 4.0",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
	install_requires=[
		"Django==4.0.2",
		"django-mptt==0.13.4",
		"django-cleanup==6.0.0",
		"pyTelegramBotAPI==4.4.0",
		"bot-storage==1.0.1",
		"loguru==0.6.0",
		"elasticsearch==7.17.0",
		"elasticsearch-dsl==7.4.0",
	]
)
