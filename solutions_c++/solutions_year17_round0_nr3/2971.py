#include <iostream>
#include<fstream>
using namespace std;

int main()
{

    FILE *fin = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/0C/C-large.in", "r", stdin);
	FILE *fout = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/0C/C-large.out", "w", stdout);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
        long long N,K,mn,mx;
        cin>>N>>K;
        long long x=0;
        while(2*x+1<K)
            x=2*x+1;
        long long g=(N+1)/(x+1);
        long long c2=N+1-g*(x+1);
        long long c1=(x+1)-c2;
        K=K-x;
        if(K>c2)
        {
            mx=(g+1)/2;
            mn=(g)/2;
        }
        else
        {
            mx=(g+2)/2;
            mn=(g+1)/2;

        }




		cout << "Case #" << t << ": ";
		cout<<mx-1<<" "<<mn-1<<endl;

	}



    return 0;
}
