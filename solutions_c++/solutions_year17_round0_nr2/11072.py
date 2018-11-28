#include <iostream>
#include <vector>

bool findIt(unsigned long long quest)
{
    std::vector<int> places;
    do {
        int place = quest % 10;
        places.push_back(place);
        quest /= 10;
    } while(quest > 0);
    for(int i = 0; i < places.size() - 1; ++i)
    {
        if(places.size() == 1)
        {
            return true;
        }
        else if(places.at(i) < places.at(i+1))
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int tasks;
    std::vector<unsigned long long> numbers;

    std::cin >> tasks;

    for(int i = 0; i < tasks; ++i)
    {
        unsigned long long thisNum;

        std::cin >> thisNum;
        numbers.push_back(thisNum);
    }

    std::vector<unsigned long long> answer;
    for(int i = 0; i < tasks; ++i)
    {
        for(int j = 0; j < numbers.at(i); ++j)
        {
            if(findIt(numbers.at(i) - j))
            {
                answer.push_back(numbers.at(i) - j);
                j = numbers.at(i);
            }
        }
    }

    for(int i = 0; i < tasks; ++i)
    {
        std::cout << "Case #" << i + 1 << ": " << answer.at(i) << std::endl;
    }
}
