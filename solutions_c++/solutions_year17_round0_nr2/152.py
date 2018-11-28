#include <stdio.h>
#include <map>
using namespace std;

long long mx = 0;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		char S[20];
		scanf ("%s",S);
		int l = 0;
		while (S[l]) l++;

		char last = '0';
		long long now = 0, mx = 0;
		for (int i=0;i<l;i++){
			now = now * 10 + S[i] - '0';
			if (S[i] > '0' && last <= S[i] - 1){
				long long u = now - 1;
				for (int j=i+1;j<l;j++) u = u * 10 + 9;
				if (mx < u)
					mx = u;
			}
			if (last > S[i]) break;
			last = S[i];
			if (mx < now)
				mx = now;
		}
		printf ("%lld\n",mx);
	}

	return 0;
}