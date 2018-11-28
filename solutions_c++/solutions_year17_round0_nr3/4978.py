#include <iostream>
#include <string>
#include <queue>

typedef uint64_t llu;
typedef int64_t ll;

using namespace std;

int main()
{
    int n = 0;
    cin >> n;

    for (int c = 0; c < n; c++)
    {
        llu s = 0, n = 0;
        cin >> s >> n;

        priority_queue<llu> q = {};
        q.push(s);

        llu idx = 0;
        llu e = 0;

        //if (n > s / 2)
        //{
        //    goto skiploop;
        //}

        while(q.size() > 0)
        { 
            e = q.top();
            q.pop();
            idx++;

            if (idx == n)
            {
                break;
            }
            if ((e % (llu)2) == (llu)0)
            {
                llu left = e / (llu)2;
                llu right = e / (llu)2;
                if (right > 0) right -= 1;

                q.push(left);
                q.push(right);
            }
            else
            {
                q.push(e / (llu)2);
                q.push(e / (llu)2);
            }
        }

    skiploop:

        llu left = e / (llu)2;
        llu right = e / (llu)2;

        if (e > 0 && (e % 2) == 0) right--;
        cout << "Case #" << c + 1 << ": " << left << " " << right << endl;
    }
    return 0;
}