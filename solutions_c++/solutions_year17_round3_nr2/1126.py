#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

struct Activity
{
    int start;
    int stop;

    bool operator<(Activity const& rhs) const
    {
        return start < rhs.start;
    }
};

double doStuff(std::vector<Activity>& A, std::vector<Activity>& C)
{
    std::sort(A.begin(), A.end());
    std::sort(C.begin(), C.end());

    // std::cout << A.size() << " " << C.size() << std::endl;
    if (A.size() + C.size() < 2 || (A.size() == 1 && C.size() == 1))
    {
        return 2;
    }
    else
    {
        std::vector<Activity>* tmp;
        if (A.size() == 2)
        {
            tmp = &A;
        }
        else if (C.size() == 2)
        {
            tmp = &C;
        }
        else
        {
            std::cout << "Error!!!" << std::endl;
            exit(1);
        }

        if (tmp->at(1).stop - tmp->at(0).start <= 720 || 1440 - (tmp->at(1).start - tmp->at(0).stop) <= 720)
        {
            return 2;
        }
        else
        {
            return 4;
        }
    }
}

int main()
{
    int nTests;
    std::cin >> nTests;
    std::cout.precision(17);

    for (int iTest = 1; iTest <= nTests; ++iTest)
    {
        int N1, N2;
        std::cin >> N1 >> N2;

        std::vector<Activity> A, C;

        for (int i = 0; i < N1; ++i)
        {
            Activity tmp;
            std::cin >> tmp.start >> tmp.stop;
            A.push_back(tmp);
        }

        for (int i = 0; i < N2; ++i)
        {
            Activity tmp;
            std::cin >> tmp.start >> tmp.stop;
            C.push_back(tmp);
        }

        std::cout << "Case #" << iTest << ": ";
        std::cout << doStuff(A, C) << std::endl;
    }

    return 0;
}