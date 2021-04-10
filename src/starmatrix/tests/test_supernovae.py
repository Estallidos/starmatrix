import pytest
import random
import numpy as np
import starmatrix.supernovae as sn


def test_empty_yields_set_is_all_zeroes():
    empty_set = sn.empty_yields_set()

    assert len(empty_set) > 0
    assert len(empty_set) == len(sn.sn_elements_list)
    for element in sn.sn_elements_list:
        assert element in empty_set.keys()
        assert empty_set[element] == 0


def test_yields_structure():
    options = ["iwa1998", "sei2013", "ln2020", "ln2018-1", "ln2018-2", "ln2018-3"]
    dataset = random.sample(options, 1)[0]
    yields = sn.yields(dataset, 0)

    assert len(yields) > 0
    assert len(yields) == len(sn.sn_elements_list)
    for element in sn.sn_elements_list:
        assert element in yields.keys()


def test_yields_from_iwamoto():
    minus1 = sn.yields_from_iwamoto(-1)
    minus0301 = sn.yields_from_iwamoto(-0.301)
    minus001 = sn.yields_from_iwamoto(-0.01)
    plus05 = sn.yields_from_iwamoto(0.5)

    assert minus1 == minus0301
    assert minus0301 != minus001
    assert minus001 == plus05


def test_yields_from_seitenzahl():
    minus2 = sn.yields_from_seitenzahl(-2)
    minus15 = sn.yields_from_seitenzahl(-1.5)
    minus1 = sn.yields_from_seitenzahl(-1)
    minus065 = sn.yields_from_seitenzahl(-0.65)
    minus03 = sn.yields_from_seitenzahl(-0.3)
    minus015 = sn.yields_from_seitenzahl(-0.15)
    minus01 = sn.yields_from_seitenzahl(-0.1)
    plus1 = sn.yields_from_seitenzahl(1)

    assert minus2 == minus15
    assert minus15 != minus1
    assert minus1 == minus065
    assert minus065 != minus03
    assert minus03 == minus015
    assert minus015 != minus01
    assert minus01 == plus1


def test_yields_from_leung_nomoto_2018():
    leung_nomoto_sources = [
        sn.yields_from_leung_nomoto_2018_table6,
        sn.yields_from_leung_nomoto_2018_table8,
        sn.yields_from_leung_nomoto_2018_table10
    ]

    for ln_dataset in leung_nomoto_sources:
        minus2 = ln_dataset(-2)
        minus165 = ln_dataset(-1.65)
        minus1 = ln_dataset(-1)
        minus065 = ln_dataset(-0.65)
        minus03 = ln_dataset(-0.3)
        minus015 = ln_dataset(-0.15)
        zero = ln_dataset(0.0)
        plus015 = ln_dataset(0.15)
        plus03 = ln_dataset(0.3)
        plus039 = ln_dataset(0.39)
        plus047 = ln_dataset(0.47)
        plus059 = ln_dataset(0.59)
        plus069 = ln_dataset(0.69)
        plus1 = ln_dataset(1)

        assert minus2 == minus165
        assert minus165 != minus1
        assert minus1 == minus065
        assert minus065 != minus03
        assert minus03 == minus015
        assert minus015 != zero
        assert zero == plus015
        assert plus015 != plus03
        assert plus03 == plus039
        assert plus039 != plus047
        assert plus047 == plus059
        assert plus059 != plus069
        assert plus069 == plus1


def test_yields_from_leung_nomoto_2020():
    minus2 = sn.yields_from_leung_nomoto_2020(-2)
    minus165 = sn.yields_from_leung_nomoto_2020(-1.65)
    minus1 = sn.yields_from_leung_nomoto_2020(-1)
    minus065 = sn.yields_from_leung_nomoto_2020(-0.65)
    minus03 = sn.yields_from_leung_nomoto_2020(-0.3)
    minus015 = sn.yields_from_leung_nomoto_2020(-0.15)
    zero = sn.yields_from_leung_nomoto_2020(0.0)
    plus015 = sn.yields_from_leung_nomoto_2020(0.15)
    plus03 = sn.yields_from_leung_nomoto_2020(0.3)
    plus039 = sn.yields_from_leung_nomoto_2020(0.39)
    plus047 = sn.yields_from_leung_nomoto_2020(0.47)
    plus059 = sn.yields_from_leung_nomoto_2020(0.59)
    plus069 = sn.yields_from_leung_nomoto_2020(0.69)
    plus1 = sn.yields_from_leung_nomoto_2020(1)

    assert minus2 == minus165
    assert minus165 != minus1
    assert minus1 == minus065
    assert minus065 != minus03
    assert minus03 == minus015
    assert minus015 != zero
    assert zero == plus015
    assert plus015 != plus03
    assert plus03 == plus039
    assert plus039 != plus047
    assert plus047 == plus059
    assert plus059 != plus069
    assert plus069 == plus1
