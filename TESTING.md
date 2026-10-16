# Testing

## Automated tests

Run the project's configured test suite from the repository root after installing its dependencies. Use the test command defined by the repository's package or build configuration; no project-specific command is listed here.

## Manual checks

- Create an inventory item with valid details and confirm it appears in the inventory.
- Edit an item and verify the changes remain after reloading or reopening the application.
- Delete an item and confirm it is no longer listed.
- Check search and filtering with matching and non-matching terms, if supported.
- Submit missing or invalid values and confirm the application reports or prevents invalid input.
- Verify existing inventory data and unrelated workflows still work after changes.

Run relevant automated tests and manually verify any affected workflows before submitting changes.
