#include <iostream>
#include <vector>

using namespace std;

int main(){

    int times;
    cin >> times;

    for(int t = 0; t < times ; t++){
        int n,k;
        cin >> n >> k;

        cout << "Case #" << t+1 << ": ";
        vector<int> blocks;
        blocks.push_back(n);
        int l,r;
        for(int i = 0; i < k; i++){
            int cur = 0;
            for(int c = 0; c < blocks.size(); c++){
                if(blocks[c] > blocks[cur]){
                    cur = c;
                }
            }


            if(blocks[cur] % 2 == 0 && blocks[cur] != 1){
                l = blocks[cur]/2 - 1;
                r = blocks[cur] - l - 1;
            }else if(blocks[cur] != 1){
                l = blocks[cur]/2;
                r = blocks[cur] - l - 1;
            }else{
                l = 0;
                r = 0;
            }
            blocks.push_back(0);
            for(int c = blocks.size()-1; c >= cur+1; c--){
                blocks[c] = blocks[c-1];
            }
            blocks[cur] = l;
            blocks[cur+1] = r;
        }
        if(l < r){
            cout << r << " " << l << endl;
        }else{
            cout << l << " " << r << endl;
        }
    }

    return 0;
}