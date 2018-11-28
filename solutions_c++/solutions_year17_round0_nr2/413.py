#include <iostream>
#include <string>
using namespace std;
string line;
int final[20];
int main()
{
    int n;
    cin >>n;
    for(int i = 1;i<=n;i++)
    {
        int count = 0;
        cin>>line;
        cout<<"Case #"<<i<<": ";
        for(int k = 0;k<line.length();k++)
        {
            final[k] = line[k]-'0';
            if(k != 0 && final[k] < final[k-1]) {
                count = k;
                break;
            }
        }
        if(count == 0)
        {
            cout<<line<<endl;
            continue;
        }
        for(count--;count>=0;count--)
        {
            final[count]--;
            if(count == 0 || final[count] >= final[count-1])
                break;
        }
        for(int k = 0;k<=count;k++)
        {
            if(final[k]!=0)
            {
                for(int p = k;p<=count;p++)
                    cout<<final[p];
                break;
            }
        }
        for(int k = count+1;k<line.length();k++)
            cout<<9;
        cout<<endl;
    }
}