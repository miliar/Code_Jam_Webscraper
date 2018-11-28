#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

string generate(int nr)
{
    string result = "";

    for(int i=0;i<nr;++i)
    {
        result+='9';
    }

    return result;
}

string tidy(string number)
{
    int strSize = number.size();

    string result = "";
    result.push_back(number[strSize-1]);

    for(int i=strSize-2;i>=0;--i)
    {

        if (number[i]>result.back())
        {
            result = generate(result.length());
            if(i != 0 )
                result.push_back(number[i]-1);
            else if(i == 0 && number[i]>'1')
            {
                result.push_back(number[i]-1);      
            }
        }
        else
        {
            if(i == 0 && number[i]<='0')
            {
                continue;
            }
            else
            {
                result.push_back(number[i]);
            }
        }
    }
    reverse(result.begin(),result.end());
    return result;
}




int main()
{
    fstream inFile("b.in",fstream::in);
    fstream outFile("b.out",fstream::out);

    int tests;
    cin>>tests;

    for(int test=1;test<=tests;++test)
    {
        string tmp;
        cin>>tmp;
        string tmpL = tidy(tmp);
        outFile<<"Case #"<<test<<": "<<tmpL<<endl;
    }

    inFile.close();
    outFile.close();


}