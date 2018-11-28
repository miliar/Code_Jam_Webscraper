#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <queue>
#include <map>

using namespace std;
char k[]="ROYGBV";
char S[1001];
int C[7];
int main()
{
    freopen( "in.txt", "r", stdin);
    freopen( "out.txt", "w", stdout);
	int T, cas = 0;
	cin>>T;
	while ( T -- )
	{
	    int N;
	    cin>>N;
	    int mx=0;
	    for ( int i =0 ; i < 6;i++)
        {
        cin>>C[i];
        mx=max(mx,C[i]);
        }
        if (mx+mx>N){
            printf("Case #%d: IMPOSSIBLE\n", ++cas);
            continue;
        }
        int j=0;
        for (int i=0;i<6;i++)
        if (C[i] == mx)
        {
            while (C[i]--)
            {
                S[j]=k[i];
                j+=2;
                if (j>=N) j=1;
            }
            C[i]=0;
        }
        for (int i=0;i<6;i++)
        if (C[i])
        {
            while (C[i]--)
            {
                S[j]=k[i];
                j+=2;
                if (j>=N) j=1;
            }
        }
        printf("Case #%d: ", ++cas);
        for (int i=0;i<N;i++) printf("%c", S[i]);
        printf("\n");
        for (int i=0;i<6;i++) if (C[i] > 0) printf("NOOOOOO\n");
        for (int i=0;i<N;i++) if (S[i] == S[(i+1)%N]) printf("NOOOOOOOOOO!\n");
	}
	return 0;
}
