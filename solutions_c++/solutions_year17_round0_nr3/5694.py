#include <iostream>

using namespace std;

pair<int,int> eval(int arr[],int ind, int n){
        int left = ind;
        while (arr[left]==0 && left>=0){
                left--;
        }
        left++;
        left = ind - left;
        int right = ind;
        while (arr[right]==0 && right<n){
                right++;
        }
        right--;
        right = right - ind;
        return {min(left,right),max(left,right)};
}

int main(){
        int t;
        cin >> t;
        int ca = 1;
        while (t--){
                int n,k;
                cin >> n >> k;
                int arr[1000050]={0};
                int num = 1;
                while (num<=k){
                        pair<int,int> MAX = {-100,-100};
                        int MAXi = -1;
                        for (int i=0;i<n;i++){
                                pair<int,int> cur = eval(arr,i,n);
                                if (cur.first>MAX.first || (cur.first == MAX.first && cur.second > MAX.second)){
                                        MAX = cur; 
                                        MAXi = i;
                                }
                        }

                        arr[MAXi] = num;
                        if (num==k){
                                cout << "Case #"<<ca++ << ": ";
                                cout << MAX.second << " " << MAX.first << endl;
                        }
                        num++;
                }
        }
}