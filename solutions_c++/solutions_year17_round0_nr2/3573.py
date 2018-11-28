#include <iostream>
#include <string>

static const char nine = '9';

void put_nine_to_remaining(std::string& str, size_t length)
{
	str.insert(str.length(), length, nine);
}

void put_nine_to_previous(std::string& str, size_t pos)
{
	static const char zero = '0';

	for (size_t i = pos; i > 0; --i)
	{
		if (str[i - 1] > str[i])
		{
			--str[i - 1];
			str[i] = nine;
		}
		else
		{
			break;
		}
	}

	if (str[0] == zero)
	{
		str = str.substr(1);
	}
}

std::string calculate_tidy_number(std::string const& number_string)
{
	std::string output;
	output.push_back(number_string[0]);
	for (size_t i = 1; i < number_string.length(); ++i)
	{
		if (output[i - 1] <= number_string[i])
		{
			output.push_back(number_string[i]);
		}
		else
		{
			--output[i - 1];
			put_nine_to_remaining(output, number_string.length() - i);
			put_nine_to_previous(output, i - 1);
			break;
		}
	}
	return output;
}

int main(void)
{
	size_t total_test_case;
	std::cin >> total_test_case;
	size_t count = 0;
	while (count < total_test_case)
	{
		std::string number_string;
		std::cin >> number_string;

		std::cout << "Case #" << count + 1 << ": " 
			<< calculate_tidy_number(number_string) << std::endl;

		++count;
	}
}