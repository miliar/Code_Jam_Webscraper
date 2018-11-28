#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isInc(int num);

int main()
{
    std::ios::sync_with_stdio(false);
    
    int t,T;
    cin >> T;
    for (t=0; t<T; t++)
    {
        int num;
        cin>>num;
        while (!isInc(num)) {
            num--;
        }
        cout <<"Case #"<<t+1<<": "<< num <<endl;
        
    }
    
    return 0;
}

bool isInc(int num)
{
    string s = to_string(num);
    if(s.size() == 1)
        return true;
    for (int i=1; i<s.size(); i++) {
        if (s[i-1]>s[i]) {
            return false;
        }
    }
    return true;
}