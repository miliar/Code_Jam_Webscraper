#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <bitset>

std::vector<std::string> extractNumbers(const std::string& path)
{
    std::string line;
    std::istringstream iss;
    std::ifstream infile(path);

    if (!std::getline(infile, line)) {
        std::cout << "Problem getting line from infile";
    }

    unsigned int nrOfTestCases;
    iss.str(line);
    iss >> nrOfTestCases;

    std::vector<std::string> numbers;
    for (unsigned int i = 0; i < nrOfTestCases; ++i) {
        std::getline(infile, line);
        numbers.push_back(line);
    }
    return numbers;
}

unsigned long long  countTiddyNumbers(const std::string& number)
{
    unsigned long long result = 0;
    
    for (unsigned long long i = 1; i <= std::strtoll(number.c_str(), NULL, 10); ++i)
    {
        std::string currentNumber = std::to_string(i);

        unsigned int min = currentNumber.front() - '0';
        for (auto& c : currentNumber)
        {
            if (min <= c - '0')
            {
                min = c - '0';
            }
            else
            {
                break;
            }

            if (&c == &currentNumber.back())
            {
                result = i;
            }
        }
    }

    return result;
}

int main()
{
    std::vector<std::string> numbers = extractNumbers("c:/input.txt");
    const unsigned int nrOfRows = numbers.size();

    //TODO: write to file
    for (unsigned int i = 0; i < nrOfRows; ++i)
    {
        std::cout << "Case #" << i + 1 << ": ";
        std::cout << countTiddyNumbers(numbers[i]);
        std::cout << std::endl;
    }

    return 0;

}
