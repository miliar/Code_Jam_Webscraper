#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int ll;

#define MAX_STALLS 1000

ll s[MAX_STALLS];
ll l[MAX_STALLS];
ll r[MAX_STALLS];
ll min_lr[MAX_STALLS];
ll max_lr[MAX_STALLS];
ll stalls;

ll get_index ()
{
	int left=0;
	l[0]=left;
	for (int i=1; i<stalls; i++)
	{
		//printf ("s[%d]=%d\n",i,s[i]);
		if (s[i] || s[i-1])
			left=0;
		else
			left++;
		l[i]=left;
		//printf ("l[%d]=%d\n",i,l[i]);
	}

	int right=0;
	r[stalls-1]=right;
	for (int i=stalls-2; i>=0; i--)
	{
		//printf ("s[%d]=%d\n",i,s[i]);
		if (s[i+1] || s[i])
			right=0;
		else
			right++;
		r[i]=right;
		//printf ("r[%d]=%d\n",i,r[i]);
	}
	
	int max_min_lr=-1;
	int max_max_lr=-1;
	int selected_index=-1;
	for (int i=0; i<stalls; i++)
	{
		if (s[i]==0)
		{

		min_lr[i]=min(l[i],r[i]);
		max_lr[i]=max(l[i],r[i]);
		if (min_lr[i]>max_min_lr)
		{
			selected_index=i;
			max_min_lr=min_lr[i];
			max_max_lr=max_lr[i];
		}
		else if ((min_lr[i]==max_min_lr)&&(max_lr[i]>max_max_lr))
		{
			selected_index=i;
			max_max_lr=max_lr[i];
		}

		}
	}
	/*
	printf ("STALLS\n");
	for (int i=0; i<stalls; i++)
		printf ("%d ", s[i]);
	printf ("\n");
	printf ("LEFT\n");
        for (int i=0; i<stalls; i++)
                printf ("%d ", l[i]);
        printf ("\n");
	printf ("RIGHT\n");
        for (int i=0; i<stalls; i++)
                printf ("%d ", r[i]);
        printf ("\n");

	printf ("selected_index=%d\n",selected_index);
	*/
	s[selected_index]=1;
	return selected_index;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		ll people;
		cin >> stalls >> people;
		printf ("Case #%d: ",i+1);
		int index;
		for (ll j=0; j<stalls; j++)
		{
			s[j]=0;
		}
		for (ll j=0; j<people; j++)
		{
			index=get_index();
		}
		printf ("%lld %lld\n",max_lr[index],min_lr[index]);
	}
}
