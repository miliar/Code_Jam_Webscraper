#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,pl,h,c,pp,m,kk,sec,yy,p,N,K,bb=0,i,j,y,z,xx,r,s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>N>>K;xx=N;
		long long int a[N+1]={0},bb=0;
		pair<int,int>b[N+1];
		for(j=1;j<=K;j++)
		{
			
			if(j==1)
			{
				if(N%2==0)
				{
					a[N/2]=1;xx=N/2;sec=xx;yy=xx;
					//cout<<"a[N/2]=="<<a[N/2]<<endl;
				}
				else
				{
					a[N/2+1]=1;xx=N/2+1;sec=xx;yy=xx;
				}
			}bb=0;r=1,s=N;
			for(p=1;j!=1 && p<=N;p++)
			{
				//cout<<"start= "<<p<< endl;
				c=0;	//cout<<"p=="<<p<<endl;
				if(bb==0 && a[p]==1)
				{
					//cout<<"p=="<<p<<endl;
					c=1;
					b[bb].first=p-r;
					//cout<<"sec=="<<sec<<endl;
					b[bb].second=(r+p)/2;
					
					if( a[r]==0 && (r+p)%2==0	)
					{
						b[bb].second-=1;
					}
					pl=b[bb].second;//cout<<"pl="<<pl<<endl;
					if(!a[pl])
					{
					//cout<<"(r+p)/2=="<<b[bb].second<<endl;
					//	cout<<"b[kk].first=="<<b[bb].first<<endl;
				//cout<<"b[kk].secc=="<<b[bb].second<<endl;
					bb++;	
					}
					
				
				}
				if(a[p]==1)
				{
					//cout<<"p=="<<p<<endl;
					for(pp=p+1;pp<=N;pp++)
					{
						
						if(a[pp]==1)
						{
							//cout<<"pp=="<<pp<<endl;
							
							yy=pp;
							b[bb].first=pp-p-1;
							b[bb].second=(pp+p)/2;
							//ut<<"ph=="<<b[bb].second<<endl;
								pl=b[bb].second;
								if(!a[pl])
								{
								//cout<<"b[kk].first=="<<b[bb].first<<endl;
								//cout<<"b[kk].secc=="<<b[bb].second<<endl;
								bb++;
							
								}
							break;	
						}
					}
					
				}
			}
			if(j!=1){
			if(1)
			{
				
				b[bb].first=s-yy;
				b[bb].second=(s+yy)/2;
				if((s+yy)%2==1)
				{
					b[bb].second+=1;
				}
				//cout<<"hh=="<<b[bb].second<<endl;
				pl=b[bb].second;
				if(!a[pl])
				{
					//cout<<"b[kk].first=="<<b[bb].first<<endl;
					//cout<<"b[kk].secc=="<<b[bb].second<<endl;
				bb++;
							
				}
				
			}
			sort(b,b+bb);
			/*for(kk=0;kk<bb;kk++)
			{
				cout<<"b[kk].first=="<<b[kk].first<<endl;
				cout<<"b[kk].secc=="<<b[kk].second<<endl;
			}*/
			m=b[bb-1].first;
			//cout<<"m==="<<m<<endl;
			for(kk=bb-1;kk>=0;kk--)
			{
				if(b[kk].first==m)
				{
					sec=b[kk].second;
				}
			}
			a[sec]=1;
			for(kk=0;kk<=N+1;kk++)
			{
				b[kk].first=0;b[kk].second=0;
			}
			//cout<<"hehe=="<<sec<<endl;	
		}
		
		}
		y=0;z=0;c=0;
		if(K==1)
		sec=xx;
		//cout<<"sec=="<<sec<<endl;
		for(h=sec+1;h<=N;h++)
		{
			if(a[h]==1)
			{
				c=1;
				y=h-sec-1;break;
			}
		}
		if(c==0)
		{
			y=N-sec;
		}c=0;
		for(h=sec-1;h>=0;h--)
		{
			if(a[h]==1)
			{
				c=1;
				z=sec-h-1;break;
			}
		}
		if(c==0)
		{
			z=sec-1;
		}
		//cout<<"y=="<<max(y,z)<<endl;
		//cout<<"z=="<<min(y,z)<<endl;
		cout<<"Case #"<<i<<": "<<max(y,z)<<" "<<min(y,z)<<endl;
	}
	
}
