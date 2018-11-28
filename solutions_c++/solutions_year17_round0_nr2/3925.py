#include <iostream>
#include <vector>

int main() {
    int num_instances;
    std::cin >> num_instances;
    for (size_t i = 0; i < num_instances; i++)
    {
        std::string number;
        std::cin >> number;
        std::vector<int> digits;
        std::vector<int> mydigits;
        for(size_t j = 0; j < number.length(); j++)
        {
            digits.push_back(number[j]-48);
            mydigits.push_back(number[j]-48);
        }

        for(int j = 0; j < mydigits.size() - 1; j++)
        {
            if(mydigits[j] > mydigits[j+1])
            {
                mydigits[j]--;
                for(int k = j+1; k < digits.size(); k+  +)
                {
                    mydigits[k] = 9;
                }
                j = -1;
            }

        }

        std::string result;

        if(mydigits.front() == 0)
        {
            mydigits.erase(mydigits.begin());
        }

        for(size_t j = 0; j < mydigits.size(); j++)
        {
            result.push_back(mydigits[j]+48);
        }

        std::cout << "Case #" << i + 1 << ": " << result << std::endl;
    }
}