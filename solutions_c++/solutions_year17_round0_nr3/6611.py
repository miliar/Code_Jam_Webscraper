#include<iostream>
#include<fstream>
using namespace std;
struct stall
{
	int stat;
	int ls;
	int rs;
	int min;
	int max;
};
int main()
{
	ifstream in("test.in");
	ofstream out("output.out");
	stall *ptr=new stall [1000002];
	stall *end,*chk,*temp,*sta;
	ptr->stat=1;
	int t,n,k,i,j,maxi,count,mini;
	in>>t;
	for(i=1;i<=t;i++)
	{
		in>>n>>k;
		end=ptr+(n+1);
		end->stat=1;
		for(temp=ptr+1;temp<end;temp++)
		temp->stat=0;
		for(j=k;j>0;j--)
		{
			for(chk=ptr+1;chk<end;chk++)
			{
				if(chk->stat==1)
				continue;
				temp=chk-1;
				while(temp>=ptr)
				{
					if(temp->stat==1)
					{
						chk->ls=(chk-temp)-1;
						break;
					}
					temp--;
				}
				temp=chk+1;
				while(temp<=end)
				{
					if(temp->stat==1)
					{
						chk->rs=(temp-chk)-1;
						break;
					}
					temp++;
				}
				if((chk->ls)>(chk->rs))
				{
					chk->max=chk->ls;
					chk->min=chk->rs;
				}
				else
				{
					chk->max=chk->rs;
					chk->min=chk->ls;
				}
			}
			mini=0;
			for(temp=ptr+1;temp<end;temp++)
			{
				if(temp->stat==1)
				continue;
				if(temp->min>mini)
					mini=temp->min;
			}
			count==0;
			for(temp=ptr+1;temp<end;temp++)
			{
				if(temp->stat==1)
				continue;
				if(temp->min==mini)
					{
						count++;
						sta=temp;
					}
			}
			if(count==1)
			sta->stat=1;
			else
			{
				maxi=0;
				for(temp=ptr+1;temp<end;temp++)
				{
					if(temp->stat==1)
					continue;
					if((temp->max>maxi)&&(temp->min==mini))
						maxi=temp->max;
				}
				count==0;
				for(temp=ptr+1;temp<end;temp++)
				{
					if(temp->stat==1)
					continue;
					if((temp->max==maxi)&&(temp->min==mini))
						{
							count++;
							sta=temp;
						}
				}
				if(count==1)
				sta->stat=1;
				else
				{
					for(temp=ptr+1;temp<end;temp++)
					{
						if(temp->stat==1)
						continue;
						if((temp->max==maxi)&&(temp->min==mini))
						{
							temp->stat=1;
							break;
						}
					}
				}	
			}
			if(j==1)
			{
				if(count==1)
					out<<"Case #"<<i<<": "<<sta->max<<" "<<sta->min<<endl;
				else
					out<<"Case #"<<i<<": "<<temp->max<<" "<<temp->min<<endl;
			}
		}
	}
	delete ptr;
	return 0;
}