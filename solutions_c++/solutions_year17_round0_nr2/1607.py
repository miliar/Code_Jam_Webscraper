#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <cstring>
typedef long long Int;
using namespace std;
bool validate(Int  t)
{
    unsigned char last=t%10;
    t=(t-t%10)/10;
    while(t!=0)
    {
        unsigned char now=t%10;
        if(now>last)
            return false;
        last=now;
        t=(t-t%10)/10;
    }
    return true;
}
Int brute_force_ans(Int st)
{
    while(!validate(st)) st--;
    return st;
}
Int solve(Int K)
{
    if(K<10)
        return K;
    if(validate(K))
        return K;
    char first[20];
    sprintf(first,"%I64u",K);
    char construct[20];
    memset(construct,0,20);
    int cur=1;
    construct[0]=first[0];
    do
    {
        construct[cur]=first[cur];
        cur++;
        if(cur>=strlen(first))
            break;
       // cout<<"comp "<<construct[cur-1]<<" "<<construct[cur-2]<<endl;
    }while(construct[cur-1]>=construct[cur-2]);
    //cout<<construct<<endl;
    cur-=2;
    while(cur>=1)
    {
        if(construct[cur]=='0'){
            cur--;
            continue;
        }
        construct[cur]--;
        if(construct[cur-1]>construct[cur])
            cur--;
        else
            break;
    }
    int rest=strlen(first);
    if(cur==0){
        if(construct[cur]=='1'){
            rest--;
            cur--;
        }else
        {
            construct[cur]--;
        }
    }
    for(int i=cur+1;i<rest;i++)
    {
        construct[i]='9';
    }
    construct[rest]='\0';
    Int out=0;
    sscanf(construct,"%I64u",&out);
    return out;
}
int main()
{
    ifstream in("B-large(1).in");
    ofstream out("A-small.out");
#define cin in
#define cout out
    int T;
    cin>>T;
    for(int iT=0;iT<T;iT++)
    {
        cerr<<iT<<"\r\r\r\r\r";
        string s;
        Int n;
        cin>>n;
        Int k=solve(n);
       /* Int k2=brute_force_ans(n);
        if(k!=k2)
        {
            cerr<<"FUCK "<<n<<" "<<k<<" "<<k2<<" ";
            k=k2;
            //cout<<endl<<endl<<"FUUUUU "<<n<<" "<<k2<<endl<<endl;
        }*/
        cout<<"Case #"<<iT+1<<": ";
        cout<<k<<endl;
    }
    return 0;
    return 0;
}
