#include <bits/stdc++.h>

using namespace std;

struct compare
{
	bool operator() (const long long &A , const long long &B)
	const
	{
		return A > B;
	}
};

long long tests , test , N , K , i , len , g;
map < long long , long long > cnt;
set < long long , compare > my;

void show(long long len)
{
    long long l , r;
    if (len % 2 == 1) l = r = len / 2;
    else l = len / 2 - 1 , r = len / 2;

    printf("%lld %lld\n" , r , l);
}

int main()
{

freopen("input" , "r" , stdin);
freopen("output" , "w" , stdout);

scanf("%lld" , &tests);
for (test = 1 ; test <= tests ; test++)
{
    scanf("%lld" , &N);
    scanf("%lld" , &K);
    printf("Case #%lld: " , test);

    my.clear() , cnt.clear();
    my.insert(N) , cnt[N] = 1;
    while (1)
    {
        len = *my.begin();
        my.erase(my.begin());
        g = cnt[len];
        if (K <= g) {show(len);break;}
        else
        {
            K -= g;
            if (len % 2 == 1)
            {
                cnt[len / 2] += 2 * g;
                my.insert(len / 2);
            }
            else
            {
                cnt[len / 2 - 1] += g;
                cnt[len / 2] += g;
                my.insert(len / 2 - 1);
                my.insert(len / 2);
            }
        }
    }

    cerr << test << '\n';
}

return 0;
}
