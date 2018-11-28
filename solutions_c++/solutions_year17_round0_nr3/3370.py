#include <iostream>
#include <set>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++)
    {
        int N, K;
        cin >> N >> K;

        set< pair<int, int> > stalls;
        stalls.insert(make_pair(-N, 0));

        for(int i = 0; i < K - 1; i++)
        {
            pair<int, int> pr = *stalls.begin();
            stalls.erase(pr);

            int sz = -pr.first;
            int startIndex = pr.second;

            pair<int, int> pr1 = make_pair(-1 * ((sz - 1) / 2), startIndex);
            pair<int, int> pr2 = make_pair(-1 * (sz / 2), startIndex + (sz - 1) / 2 + 1);
            stalls.insert(pr1);
            stalls.insert(pr2);
        }

        int sz = -stalls.begin()->first;
        int res1 = sz / 2;
        int res2 = (sz - 1) / 2;

        cout << "Case #" << t << ": " << res1 << " " << res2 << endl;
    }

    return 0;
}