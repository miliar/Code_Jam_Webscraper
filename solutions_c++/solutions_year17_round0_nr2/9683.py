#include<bits/stdc++.h>
#include<string>
using namespace std;
int length(long long N)
{
    int i;
    for(i=0;i<=18;i++)
        if(N<pow(10,i))
            return i;
}
string numToString(long long N)
{
    string res="";
    for(int i=0;i<length(N);i++)
    {
        long long cur=N/pow(10,i);
    }
}
string rec(string ini,string res,int cur)
{
    if(ini[cur]<res[cur])
        for(int i=0;i<18;i++)
    {
        res[cur]=ini[cur]-i;
        if(res[cur]!='*')
            return res;
    }

}
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");
    int T;
    fin>>T;
    int iniT=T;
    while(T--)
    {
        long long N;
        fin>>N;
        stringstream ss;
        ss << N;
        string ini = ss.str();
        //string ini=to_string(N);
        string res="";
        for(int i=0;i<ini.size();i++)
            res+=ini[i];
        //res[0]='0';
        for(int i=0;i<ini.size()-1;i++)
        {
            if(ini[i]>res[i+1])
            {//cout<<i;
                res[i]=res[i]-1;
                for(int j=0;j<i;j++)
                {
                    if(res[j]>res[i])
                    {
                        i=j;
                        res[i]=res[i]-1;
                        break;
                    }
                }
                //cout<<i<<endl;
                for(int j=i+1;j<ini.size();j++)
                    res[j]='9';
            }

        }
        bool st=false;

        fout<<"Case #"<<iniT-T<<": ";
        for(int i=0;i<res.size();i++)
            {
                if(res[i]!='0')st=true;
                if(st)fout<<res[i];
                //else if()
            }
            fout<<endl;

//        cout<<rec(ini,res,0);
//        bool need=true;
//        for(int i=0;i<ini.size();i++)
//        {
//            if(need&&ini[i]>res[i])
//            {
//                res[i]=ini[i];
//                need=false;
//            }
//            if(!need)
//            {
//
//            }
//        }

    }
    fout.close();
}
