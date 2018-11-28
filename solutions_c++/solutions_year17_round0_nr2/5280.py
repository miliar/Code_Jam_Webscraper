#include <iostream>
#include <string>

using namespace std;

int main(void){
    string inp_str;
    string::size_type sz=0;
    long long inp_ll;
    int kase;
    int inp_len;
    cin >> kase;
    for(int cs = 1; cs <= kase; cs++){
        cin >> inp_str;
        inp_len = inp_str.size();
        int cur = 0;
        while(cur < inp_len-1 && inp_str[cur] <= inp_str[cur+1]) cur++;
        if(cur != inp_len-1){
            while(cur > 0  && inp_str[cur] == inp_str[cur-1]) cur--;
            for(int cur_end = cur+1; cur_end < inp_len; cur_end++) inp_str[cur_end] = '0';
            inp_ll = stoll(inp_str, &sz, 10);
            inp_ll--;
        }
        else inp_ll = stoll(inp_str, &sz, 10);
        cout << "Case #" << cs << ": " << inp_ll << endl;
    }
    return 0;
}
