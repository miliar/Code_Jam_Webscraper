#include <iostream>
#include <fstream>
#include <queue>

int main()
{
    std::ifstream input("data3.txt");
    std::ofstream output("res3.txt");

    int T = 0;

    input >> T;

    for (int i = 0; i < T; ++i)
    {
        unsigned long N = 0;
        unsigned long K = 0;

        input >> N;
        input >> K;

        std::priority_queue<unsigned long> q;
        q.push(N);

        unsigned long left = 0;
        unsigned long right = 0;

        while (!q.empty() && K != 0)
        {
            unsigned long tmp = q.top();

            if (tmp % 2 == 0)
            {
                left = tmp / 2 - 1;
                right = tmp / 2;
            }
            else
            {
                left = tmp / 2;
                right = left;
            }

            if (right > 1)
            {
                q.push(right);
                q.push(left);
            }

            q.pop();

            --K;
        }

        if (q.empty() && K != 0)
            output << "Case #" << i + 1 << ": 0 0" << std::endl;
        else
            output << "Case #" << i + 1 << ": " << right << " " << left << std::endl;
    }

    input.close();
    output.close();
}
