#include <iostream>
#include <cstdio>  
#include <iostream>  
#include <string>  
#include <iterator>  
#include <algorithm>  
#include <vector>  
#include <cstring>  
#include <array>  
#include <queue>  
#include <set>  
#include <map>  
using namespace std;


string solve(string& s, int size, int count) {
    int flip = 0;
    for(int i=0;i<=s.size() - size;i++) {
        if(s[i] == '-') {
            int count_neg = 0, count_pos = 0;
            for(int j=i;j<i+size;j++) {
                if(s[j] == '-') {
                    s[j] = '+';
                    count_neg++;
                }
                else {
                    s[j] = '-';
                    count_pos++;
                }
            }
            flip++;
            count += (count_neg - count_pos);
        }
    }
    if(count == s.size())
        return to_string(flip);
    else
        return "IMPOSSIBLE";

}

// char val[1010] = {0};

int main()  
{  
    freopen("A-large.in.txt", "r", stdin);  
    //freopen("in.txt", "r",stdin);  
    freopen("out.txt", "w", stdout);  
    int t;  
    scanf("%d", &t);  
    int size;
    string val;
    for (int i = 1; i<= t; i++)  
    {  
        cin>>val;
        cin>>size;
        // count for +
        int count = 0;
        for(auto c : val)
            if(c == '+')
                count++;
        printf("Case #%d: ", i);
        string res = solve(val, size, count);
        cout<<res<<endl;
    }  
    return 0;  
}  