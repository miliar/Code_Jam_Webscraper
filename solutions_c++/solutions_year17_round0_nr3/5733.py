#include <iostream>
using namespace std;
int main()
{
	int T, N, K, x, y, z, i, j, mx, per, pos;
	bool bs[1002];
	int min[1002], max[1002], l[1002], r[1002];
	cin >> T;
	for(x=1; x<=T; x++)
	{
		cin >> N >> K;
		if(N==K)
		{
			y=0;
			z=0;
		}
		else if(K==1)
		{
			y=N/2;
			z=(N-1)/2;
		}
		else
		{
		bs[0]=true;
		bs[N+1]=true;
		for(i=1; i<=N; i++)
			bs[i]=false;
		for(per=1; per<=K; per++)
		{
			for(i=0; i<=N+1; i++)
			{
				if(!bs[i])
				{
					for(j=i-1, l[i]=0; !bs[j]; j--)
						l[i]++;
					for(j=i+1, r[i]=0; !bs[j]; j++)
						r[i]++;
					min[i]=(l[i]<r[i])?l[i]:r[i];
				}
				else
					min[i]=-1;
			}
			mx=min[1];
			for(i=2; i<=N; i++)
				if(!bs[i] && min[i]>mx)
					mx=min[i];
			for(pos=1; min[pos]!=mx; pos++);
			for(i=pos+1; i<=N; i++)
				if(!bs[i] && min[i]==mx)
					break;
			if(i<=N)
			{
				for(i=0; i<=N+1; i++)
				{
					if(!bs[i] && min[i]==mx)
					{
						for(j=i-1, l[i]=0; !bs[j]; j--)
							l[i]++;
						for(j=i+1, r[i]=0; !bs[j]; j++)
							r[i]++;
						max[i]=(l[i]>r[i])?l[i]:r[i];
					}
					else
						max[i]=-1;
				}
				pos=1;
				mx=max[pos];
				for(i=2; i<=N; i++)
					if(!bs[i] && max[i]>mx)
					{
						pos=i;
						mx=max[pos];
					}
			}
			bs[pos]=true;
		}
		y=(l[pos]>r[pos])?l[pos]:r[pos];
		z=(l[pos]<r[pos])?l[pos]:r[pos];
		}
		cout << "Case #" << x << ": " << y << " " << z << endl;
	}
	return 0;
}