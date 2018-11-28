#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t, i, n, temp, y, pre = 10000;
    vector<int> vec;
    cin>>t;
    for(i=0;i<t;i++)
    {
            cin>>n;
            temp = n;
            pre = 1000;
            while(temp)
            {
                y = temp%10;
                temp = temp/10;
                if(y > pre){
                    temp = n = n-1;
                    pre = 1000;
                    }
                else{
                    pre = y;
                }
            }
            vec.push_back(n);
    }
    for(int i = 0; i < vec.size(); i++){
        cout<<"Case #"<<i+1<<": "<<vec.at(i)<<endl;
    }
    return 0;
}
