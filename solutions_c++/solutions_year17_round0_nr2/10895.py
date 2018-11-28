#include<iostream>
using namespace std;

int main()
{
//freopen("input_file_name.in","r",stdin);
//freopen("output_file_name.out","w",stdout);

    int t;
    cin>>t;
int answer[t+1];
    for(int i=1;i<=t;i++)
    {
        long long int n,r1,temp;
        cin>>n;
      for(long long int j=n;j>=1;j--)
      {
      long long int k=j;
       temp=k%10;
       k=k/10;
      // cout<<"k==="<<k<<endl;
    //  cout<<"loopstart"<<endl;
      bool flag=true;
       while(k!=0)
       {
        r1=k%10;
        k=k/10;
    //    cout<<"k==="<<k<<endl;
        if(r1<=temp){
            temp=r1;
            continue;
        }
        else
        {
            flag=false;
            break;
        }

       }
     //  cout<<"outerloop"<<endl;
    //  cout<<"k==="<<k<<endl;
       if(k==0 && flag==true)
       {
           answer[i]=j;
           break;
       }
      }
    }

    for(int i=1;i<=t;i++)
    cout<<"Case #"<<i<<": "<<answer[i]<<endl;
}
