#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	//ofstream fout("C:\\rei\\Document.txt");
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
    int n,k;
    string ss;
    cin>>ss>>k;
    vector<int> v;
    n=ss.size();
    for(int i=0;i<n;i++)
    {
        if(ss[i]=='+')
        v.push_back(1);
        else
        v.push_back(0);
    }
    int brojac1=0;
    int brojac2=0;
    vector<int> v1(n+1,0);
    int zbir1=0;
    int zbir2=0;
    vector<int> v2(n+1,0);
    /*for(int i=0;i<n;i++)
    {
        if((v[i]+zbir1)%2!=0)
        {
            v1[i]=1;
        }
        if(i>=k-1)
            zbir1+=v1[i]-v1[i-k+1];
        else
            zbir1+=v1[i];
        brojac1+=v1[i];
        if(i>n-k&&v1[i]!=0){
            brojac1=1e9;
            break;
        }
    }*/
    for(int i=0;i<n;i++)
    {
        if((v[i]+zbir2)%2!=1)
        {
            v2[i]=1;
        }
        if(i>=k-1)
            zbir2+=v2[i]-v2[i-k+1];
        else
            zbir2+=v2[i];
        brojac2+=v2[i];
        if(i>n-k&&v2[i]!=0){
            brojac2=1e9;
            break;
        }
    }
    int brojac=brojac2;
    cout<<"Case #"<<ii<<": ";
    if(brojac==1e9)
    {
        cout<<"IMPOSSIBLE"<<endl;
    }
    else
    {
        cout<<brojac<<endl;
    }
    }
    return 0;
}