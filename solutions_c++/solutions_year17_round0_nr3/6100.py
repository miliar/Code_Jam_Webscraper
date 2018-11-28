#include<iostream>
#include<vector>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
    long t,i=1,l,j,x,y,n,k;
    cin>>t;
    while(i<=t){
        l=1;
        cin>>n>>k;
        vector<long>a;
        a.push_back(n);
        long max=a[0];
        long index=0;
        while(k!=0){
            
            if(max%2==0){
                a.push_back(max/2);
                a.push_back(max/2-1);
            }
            else{
                a.push_back(max/2);
                a.push_back(max/2);
            }
            l+=2;
            k--;
            a[index]=-1;
            max=a[0];
            for(j=0;j<l;j++){
                if(max<a[j]){
                    max=a[j];
                    index=j;
                }
            }
            
        }#include<bits/stdc++.h>
using namespace std;
int main()
{int z,t;
cin>>t;
for(z=0;z<t;z++)
{ std::priority_queue<int> a;
int b,c,d,e,i,f;
cin>>e;
a.push(e);
cin>>b;
for(i=0;i<b;i++)
{f=a.top();
    c=f/2;
d=(f-1)/2;
a.push(c);
a.push(d);
a.pop();
}
 cout<<"Case #"<<z+1<<":"<<" "<<c<<" "<<d<<"\n";   

}
}

        if(k==0){
                 l=a.size();
                 x=a[l-1];
                 y=a[l-2];
                if(x>y){
                    printf("Case #%ld: %ld %ld\n",i,x,y);
                   
                }
                else
                    printf("Case #%ld: %ld %ld\n",i,y,x);
                   
            }
        i++;
    }
    return 0;
}