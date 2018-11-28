#include <bits/stdc++.h>

#define MOD 1000000009

using namespace std;

int readInt () {
	bool minus = false;
	int result = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
	if (minus)
		return -result;
	else
		return result;
}

int main()
{
    freopen("D:/codes/in.txt","r",stdin);
    freopen("D:/codes/out.txt","w",stdout);

    int t,n,i,j,cnt,dist,d;
    int k[1001],s[1001];

     scanf("%d",&t);
     int tc=t;
     while(t--)
     {
        printf("Case #%d: ",tc-t);
        scanf("%d%d",&d,&n);

        for(i=0;i<n;++i)
        {
            k[i]=readInt();
            s[i]=readInt();
        }

        double m=0,time=0,ans;
        for(i=0;i<n;++i)
        {
            dist=d-k[i];
            time=(double)dist/s[i];
            if(m<time)
                m=time;
        }

        ans=d/m;


         printf("%f\n",ans);

     }

	return 0;

}
