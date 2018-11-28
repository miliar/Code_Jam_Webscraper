#include<bits/stdc++.h>
using namespace std;
map<long long int,long long int> mymap;
int main()
{
    	freopen("input3.txt", "r", stdin);
   	freopen("output3.txt", "w", stdout);
	int T = 1;
	scanf("%d",&T);
	for(int test=1;test<=T;++test)
	{
	mymap.clear();
        long long int N,K;
        scanf("%lld",&N);
        scanf("%lld",&K);
        mymap[N] = 1;
        K--;
        while( K>=0 ) {
            map<long long int,long long int> ::reverse_iterator it = mymap.rbegin();
            long long int len = it -> first;
            long long int cnt = it -> second;
            if(cnt > K) {
                long long int row, col;
                if(len%2==0) {
                    col=(len - 1) / 2;
                    row=len / 2;
                }
                else
		{
                   	row = len / 2;
			col = len / 2;
                }
                printf("Case #%d: %lld %lld\n", test, row, col);
                break;
            }
            else 
	    {

                mymap.erase(mymap.find(len));
                K = K-cnt;
                long long int length1, length2;
                if(len%2 == 0) 
		{
                    length1 = (len - 1) / 2;
                    length2 = len / 2;
                }
                else
		{
                        length1 = len / 2;
			length2 = len / 2;
                }

                if(length1>0) {
                    if(mymap.find(length1) != mymap.end()) 
		    {
                        mymap[length1] += cnt;
                    }
                    else
		    {
                        mymap[length1] = cnt;
                    }
                }

                if(length2>0) 
 		{
                    if(mymap.find(length2) != mymap.end()) 
		    {
                        mymap[length2] += cnt;
                    }
                    else{
                        mymap[length2] = cnt;
                    }
                }
            }
        }
    }
	return 0;
}
