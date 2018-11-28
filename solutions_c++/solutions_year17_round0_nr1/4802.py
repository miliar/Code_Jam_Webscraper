#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;


int main(){
    fstream outFile("a.out",fstream::out);

    int tests;
    cin>>tests;

    for(int test=1;test<=tests;++test)
    {
        string pancakes;
        int k;
        cin>>pancakes>>k;

        outFile<<"Case #"<<test<<": ";

        int count = 0;
        for(int i=0;i<=pancakes.size()-k;++i)
        {
            if (pancakes[i] == '-')
            {
                count++;

                for(int j=i;j<i+k;++j)
                {
                    if(pancakes[j]=='-')
                    {
                        pancakes[j] = '+';
                    }
                    else
                    {
                        pancakes[j] = '-';
                    }
                }
            }
        }
        
        bool isHappy = true;

        for(int i=pancakes.size()-k;i<pancakes.size();++i)
        {
            if(pancakes[i] == '-')
            {
                isHappy = false;
                break;
            }
        }

        if(isHappy)
        {
            outFile<<count<<endl;
        }
        else
        {
            outFile<<"IMPOSSIBLE"<<endl;
        }

    }


}