
#include<stdio.h>
struct data
{
	int left;
	int right;
};
struct value
{
	int value;
	int index;
};
int leftfunction(int low,int high, int index)
{
				int k,count;
				k=index;		
				count=0;				
				while(k>low+1)	
				{
					count++;			
					k--;
				}

				return count;
}
int rightfunction(int low,int high, int index)
{
				int c,count1;
				c=index;
				count1=0;
				while(c<high-1)
				{
					count1++;
					c++;				
				}
				return count1;
}
int main()
{
	int t,n,h,m,l,i,low,high,A[10000],one[10000],same[10000],d,s,te,same1[1000],da,out;
	scanf("%d",&t);
	for(int o=1;o<=t;o++)
	{
		struct data B[10000];
int output;
		struct value min[10000],max[10000];
		scanf("%d %d",&n,&m);
		A[0]=1;
		A[n+1]=1;			
		for(i=1;i<=n;i++)
		{
			A[i]=0;
		}
		
		for(int ha=1;ha<=m;ha++)
		{
		d=1;		
		for(i=0;i<=n+1;i++)
		{
			if(A[i]==1)
			{
				one[d]=i;
				d++;
			}
		}
		for(h=0;h<=n+1;h++)
		{					
			if(A[h]==0)
			{
				for(s=1;s<d;s++)
				{
					if(one[s]<h)
					{
						low=one[s];
					}
				}
				for(s=d-1;s>=1;s--)
				{
					if(one[s]>h)
					{
						high=one[s];
					}
				}
				B[h].left=leftfunction(low,high,h);
				B[h].right=rightfunction(low,high,h);				
			}
			
		}
		/*for(h=1;h<=n;h++)
		{
			if(A[h]==0)
			printf("%d %d %d\n",B[h].left,B[h].right,h);
		}*/
		int	p=1;
		for(h=1;h<=n;h++)
		{
			if(A[h]==0)
			{
				if(B[h].left<=B[h].right)
				{
					min[p].value=B[h].left;
					min[p].index=h;
					//printf("%d\n",min[p].value);
				}
				if(B[h].left>B[h].right)
				{
					min[p].value=B[h].right;
					min[p].index=h;
					//printf("%d\n",min[p].value);
				}
				if(B[h].left<=B[h].right)
				{
					max[h].value=B[h].right;
					max[h].index=h;
					//printf("%d\n",max[p].value);
				}
				if(B[h].left>B[h].right)
				{
					max[h].value=B[h].left;
					max[h].index=h;
					//printf("%d\n",max[p].value);
				}
				p++;
			}
		}
		int su=1;
	int	less=min[1].value;
		same[su]=min[1].index;
		for(te=2;te<p;te++)
		{
			if(less<min[te].value)
			{
				su=1;
				less=min[te].value;
				same[su]=min[te].index;
				
			}
			else if(less==min[te].value)
			{
				su++;
				same[su]=min[te].index;
				
			}
		}
		if(su==1)
		{
			int vi=same[su];
			A[vi]=1;
			output=vi;
		}
		
		else
		{
			
			int ch=1;
			int ra=same[1];
			int more=max[ra].value;
			same1[ch]=max[ra].index;
			for(te=2;te<=su;te++)
			{
				ra=same[te];
				if(more<max[ra].value)
				{
					ch=1;
					more=max[ra].value;
					same1[ch]=max[ra].index;
				}
				else if(more==max[ra].value)
				{
					ch++;
					same1[ch]=max[ra].index;
				}
			}

			/*for(h=1;h<=ch;h++)*/	
		//printf("%d\n",ch);	
			if(ch==1)
			{
				ra=same1[ch];
				A[ra]=1;
				output=ra;
			}
			else
			{
				int na=same1[1];
				out=B[na].left;
				 int da=na;
				
				for(te=2;te<=ch;te++)
				{
					na=same1[te];
					
					if(out>B[na].left)
					{
						out=B[na].left;
						da=na;
					}
				}
				//printf("%d\n",da);
				A[da]=1;
				 output=da;
				
			}
		}
		//printf("%d\n",output);
		if(ha==m)
		{
			printf("case #%d: %d %d\n",o,B[output].right,B[output].left);
		}
	}
	}
}
