#include<iostream>
#include<string>
#include<algorithm>
#include<cstdlib>
#include<fstream>
#include<cstdio>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("in.txt",ios::in);
    /*if(!fin){
        cout<<"cannot open a file \n";
    return 1;}*/
    ofstream output;
    output.open("output.txt",ios::out);


    int t,it;
    fin>>t;//cout<<t;
    for(it=0;it<t;it++){
    string s;
    int i,k,l,c=0,co,j;
    fin>>s>>k;//cout<<s<<k;
    l=s.length();
    //output<<l;
    for(i=0;i<l;i++)
    {
        if(s[i]=='-' && (l-i)>=k)
        {
            c++;
            for(j=i;j<k+i;j++)
            {
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
            }

        }
    }
    //output<<s;
    co= count(s.begin(),s.end(),'-');
    //output<<co<<" ";
    if(co==0)
        output<<"Case #"<<(it+1)<<": "<<c<<"\n";
    else
        output<<"Case #"<<(it+1)<<": "<<"IMPOSSIBLE"<<"\n";
}
fin.close();
output.close();
}
