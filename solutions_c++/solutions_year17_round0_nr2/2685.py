#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    std::ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    string str;
    int nums[20];
    cin>>t;
    for(int cc = 1; cc <= t; ++cc){
        cin>>str;
        int len = str.size();
        for(int i = 0; i < len; ++i)
            nums[i] = str[i] - '0';
        int first_pos = -1;
        int prev_num = 0;
        for(int i = 0; i < len; ++i){
            if(nums[i] < prev_num){
                first_pos = i;
                break;
            }
            prev_num = nums[i];
        }
        //cout<<first_pos<<endl;
        if(first_pos == -1){
            cout<<"Case #"<<cc<<": ";
            for(int i = 0; i < len; ++i)
                cout<<nums[i];
            cout<<endl;
        } else{
            first_pos++;
            for(int i = len; i > 0; --i)
                nums[i] = nums[i-1];
            nums[0] = 0;

            bool found = false;
            for(int i = first_pos; i > 0; --i){
                if(nums[i] - 1 >= nums[i - 1]){
                    nums[i]--;
                    for(int j = i + 1; j <= len; ++j)
                        nums[j] = 9;
                    break;
                }
            }
            int beg;
            if(nums[1] == 0)
                beg = 2;
            else
                beg = 1;
            cout<<"Case #"<<cc<<": ";
            for(int i = beg; i <= len; ++i)
                cout<<nums[i];
            cout<<endl;
        }
    }

    return 0;
}
