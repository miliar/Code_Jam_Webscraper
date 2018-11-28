#include <iostream>
#include <string>

using namespace std;

int check(string s)
{
    int i,count=0;
    for(i=1;s[i]!='\0';i++)
    {
        if(s[i-1]>s[i])
        {
            count=1;
            //cout<<"count";
            break;
        }
    }
    if(count==0)
        {
           // cout<<"tidy";
            return 1;
        }
    else
    {
        //cout<<"non";
        return 0;
    }

}


int main()
{
    std::string s;
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {


    cin>>s;

    while(check(s)!=1)
    {
                string::iterator it=s.end();
                it--;


                    while(*it=='0')
                    {
                        //cout<<"while1 ";
                        *it='9';
                        it--;
                    }
                    (*it)--;
                    //cout<<s<<" ";
    }
    string::iterator it=s.begin();
    if(*it=='0')
    s.erase(it);

    cout<<"Case #"<<j<<":"<<" "<<s<<endl;

    }
    return 0;
}

