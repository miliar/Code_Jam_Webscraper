#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    ifstream in ("cjB.in");
    ofstream out ("cjB.out");
    
    long t;
    in >> t;
    for(long q=1; q<=t; q++){
        // cout << "Z " << q << endl;
        long n;
        in >> n;
        long r, o, y, g, b, v;
        in >> r >> o >> y >> g >> b >> v;
        string ans = "";
        string ord;
        if(r>=b && b>=y){
            ord = "RBY";
        }
        else if(r>=y && y>=b){
            ord = "RYB";
        }
        else if(b>=y && y>=r){
            ord = "BYR";
        }
        else if(b>=r && r>=y){
            ord = "BRY";
        }
        else if(y>=r && r>=b){
            ord = "YRB";
        }
        else{
            ord = "YBR";
        }
        long nums[3];
        nums[0] = -r;
        nums[1] = -y;
        nums[2] = -b;
        sort(nums,nums+3);
        for(long i = 0; i<3; i++){
            nums[i] = -nums[i];
        }
        bool ok = true;
        // cout << "Z" << endl;
        long count = 0;
        bool theory = nums[0]<=(nums[1]+nums[2]);
        while(true){
            count ++;
            // if(count==8){
                
            //     break;
            // }
            // cout << "HI" << endl;
            // cout << nums[0] << " " << nums[1] << " " <<nums[2] << " " << ans << endl;
            if(nums[0] ==0 && nums[1]==0 && nums[2]==0){
                break;
            }
            if(nums[0]==nums[1] && nums[1]==nums[2]){
                ans += ord;
                for(long i = 0; i<3; i++){
                    nums[i]--;
                }
                continue;
            }
            if(nums[0]==nums[1]){
                ans += ord.substr(0,1);
                ans += ord.substr(1,1);
                for(long i = 0; i<2; i++){
                    nums[i]--;
                }
                continue;
            }
            if(nums[1]>=nums[2] && nums[1]>0){
                ans += ord.substr(0,1);
                ans += ord.substr(1,1);
                for(long i = 0; i<2; i++){
                    nums[i]--;
                }
                continue;
            }
            if(nums[2]>nums[1]){
                ans += ord.substr(0,1);
                ans += ord.substr(2,1);
                nums[0]--;
                nums[2]--;
                continue;
            }
            ok = false;
            break;
        }
        out << "Case #" << q <<": ";
        if(ans.length()!=n && ok){
            cout << "!!!" << endl;
            cout << ans.length() << " " << n << endl;
        }
        if(!ok){
            out << "IMPOSSIBLE";
        }
        else{
            out << ans;
        }
        out << endl;
    }
    
    return 0;
}