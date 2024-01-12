from nrgpy import logr_read


class TestLogrRead:
    def test_logr_concat_9431_returns(self, test_file_directory):
        """Check that LOGR-S (model 9431) dat files are ingested by nrgpy.logr_read"""
        reader = logr_read()
        reader.concat_txt(dat_dir=str(test_file_directory), file_filter="000511")

        assert reader.site_description == "Crows Nest", f"Expected site number {reader.site_description} to be 'Crows Nest'"
        assert len(reader.data) == 180, f"Dataframe length {len(reader.data)} is not 180"

    def test_logr_concat_9432_returns(self, test_file_directory):
        """Check that LOGR|SOLAR (model 9432) dat files are ingested by nrgpy.logr_read"""
        reader = logr_read()
        reader.concat_txt(dat_dir=str(test_file_directory), file_filter="000304")

        assert reader.site_description == "Crows Nest Counters", f"Expected site number {reader.site_description} to be 'Crows Nest'"
        assert len(reader.data) == 41, f"Dataframe length {len(reader.data)} is not 180"

    def test_logr_read_9432_log_returns(self, test_file_directory):
        """Check that LOGR|SOLAR (model 9432) log files are ingested by nrgpy.logr_read"""
        filename = test_file_directory / "20240111_1339_000304_002995.log"
        reader = logr_read(filename, drop_duplicates=False)

        assert reader.site_description == "Crows Nest Counters", f"Expected site description {reader.site_description} to be 'Crows Nest Counters'"
        assert len(reader.data) == 1, f"Dataframe length {len(reader.data)} is not 1"

    def test_logr_concat_9432_log_returns(self, test_file_directory):
        """Check that LOGR|SOLAR (model 9432) log files are ingested by nrgpy.logr_read"""
        reader = logr_read()
        reader.concat_txt(
            dat_dir=str(test_file_directory),
            file_type="log",
            file_filter="000304",
            drop_duplicates=False,
        )

        assert reader.site_description == "Crows Nest Counters", f"Expected site description {reader.site_description} to be 'Crows Nest Counters'"
        assert len(reader.data) == 3, f"Dataframe length {len(reader.data)} is not 3"
