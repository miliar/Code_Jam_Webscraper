#include <bits/stdc++.h>
using namespace std;
int stringtoint(string s){
istringstream buffer(s);
int value;
buffer >> value;
return value;
}
string IntToString (int a)
{
    ostringstream temp;
    temp<<a;
    return temp.str();
}
int main()
{
freopen("B-large.in","rt",stdin);
freopen("out.txt","wt",stdout);
int n;
cin>>n;
string s;
for(int i=0;i<n;i++)
{
    cin>>s;
//    cout<<s<<" ";
//    int tr=stringtoint(s);
//    for(int i=tr;i>=0;i--)
//    {
//        string lel=IntToString(i);
//        int c='0';
//        bool bla=true;
//        for(int j=0;j<lel.size();j++)
//        {
//            if(lel[j]>=c)
//                c=lel[j];
//            else {
//                bla=false;
//                break;
//            }
//        }
//        if(bla){
//            cout<<i<<" ";
//            break;
//        }
//    }
    char c='0';
    int pos=-1;
    for(int j=0;j<s.size();j++)
    {
        if(s[j]>=c)
            c=s[j];
        else {
            pos=j;
            break;
        }
    }
    if(pos!=-1){
    for(int j=pos;j<s.size();j++)
        s[j]='9';
    int j;
    for(j=pos-1;j>0;j--)
    {
        int x=s[j]-'0';
        x--;
        s[j]=x+'0';
        if(s[j]=='0')
            s[j]='9';
        if(s[j]>=s[j-1]&&s[j]!='9')
            break;
        else s[j]='9';
    }
    if(j==0&&s[j+1]=='9'){
        int y=s[j]-'0';
        y--;
        s[j]=y+'0';
        }
    }
    string ne="";
    if(s[0]!='0')
        ne+=s[0];
    for(int j=1;j<s.size();j++)
        ne+=s[j];
    cout<<"Case #"<<i+1<<": "<<ne<<endl;
}

}
