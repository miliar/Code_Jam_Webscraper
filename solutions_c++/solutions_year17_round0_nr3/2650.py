#include<iostream>
#include<bits/stdc++.h>
using namespace std;
struct node{
    long long a,cnt;
};
int main()
{
        long long t;

        cin>>t;
        for(long long i=1;i<=t;i++)
        {
            long long n,k,temp1,temp2;
            cin>>n>>k;
            set<pair<long long,long long> > p;
            p.insert(make_pair(n,1));
            while(k)
            {
                set<pair<long long,long long> >:: reverse_iterator rit = p.rbegin();
                temp1=(*rit).first;
                temp2=(*rit).second;
                //cout<<temp1<<endl<<temp2<<endl;
                if(k<=temp2)
                    break;
                p.erase(make_pair(temp1,temp2));
                if(temp1%2==0)
                {
                    set<pair<long long,long long> >:: iterator it = p.begin();
                    long long temp=0;
                    for(;it!=p.end();it++)
                    {
                        if((*it).first==temp1/2)
                        {
                            temp= (*it).second;
                            p.erase(it);
                            break;
                        }
                    }
                        p.insert(make_pair((temp1/2),temp2+temp));
                    temp=0;
                    it=p.begin();
                    for(;it!=p.end();it++)
                    {
                        if((*it).first==(temp1/2-1))
                        {
                            temp= (*it).second;
                            p.erase(it);
                            break;
                        }
                    }
                        p.insert(make_pair(((temp1/2)-1),temp2));
                }
                else
                {
                    set<pair<long long,long long> >:: iterator it = p.begin();
                    long long temp=0;
                    for(;it!=p.end();it++)
                    {
                        if((*it).first==temp1/2)
                        {
                            temp= (*it).second;
                            p.erase(it);
                            break;
                        }
                    }
                        p.insert(make_pair((temp1/2),(temp2*2)+temp));
                }
                k-=temp2;
            }
            set<pair<long long,long long> >:: reverse_iterator rit = p.rbegin();
                temp1=(*rit).first;
            if(temp1%2==0)
                {
                   temp1=temp1/2;
                   temp2=temp1-1;
                }
                else
                {
                    temp1=temp1/2;
                    temp2=temp1;
                }
            cout<<"Case #"<<i<<": "<<temp1<<" "<<temp2<<endl;
        }
    return 0;
}
