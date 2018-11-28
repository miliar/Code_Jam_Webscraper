#include<fstream>
#include<map>
int main(){

    std::ofstream cout;
    cout.open("C:\\C-small-2-attempt1.out");
    std::ifstream cin;
    cin.open("C:\\C-small-2-attempt1.in");

    int T;
    cin >> T;
    for(int t=1; t<=T; t++){
        std::map<int64_t,int> emptyRooms;
        int64_t N,K;
        cin >> N >> K;
        int64_t min,max;
        int cnt = 0;
        emptyRooms[-N]++;
        while(cnt < K){
            int64_t val = emptyRooms.begin()->second;
            int64_t key = emptyRooms.begin()->first;
            key = -key;
            emptyRooms.erase(emptyRooms.begin());
            max = key/2;
            min = key - 1 - max;
            emptyRooms[-min]+=val;
            emptyRooms[-max]+=val;
            cnt+=val;
        }
        cout << "Case #" << t << ": "<< max << " " << min << "\n";
    }

    cin.close();
    cout.close();
}
