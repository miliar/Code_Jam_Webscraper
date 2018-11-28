#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
typedef long long ll;
string process(string num)
{
    if (num[0] == '0') return num.substr(1);
    bool order = true;
    int index = 1000000000;
    for (int i = 1; i < num.size(); i++)
    {
        if (num[i] < num[i-1])
            order = false;
        if (num[i] < num[i-1])
            index = min(index, i);
    }
    if (order) return num;
    for (int i = index; i < num.size(); i++)
        num[i] = '9';
    while (true)
    {
        if (num[index-1] == '0')
        {
            num[index-1] = '9';
            index--;
        }
        else
        {
            num[index-1] -= 1;
            break;
        }
    }
    return process(num);
}
int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++)
    {
        char num[20];
        scanf("%s", num);
        printf("Case #%d: ", z);
        printf("%s\n", process(string(num)).c_str());
    }
    return 0;
}
