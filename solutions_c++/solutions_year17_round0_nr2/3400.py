#include "iostream"
#include "string"


using namespace std;

int sub(int num[],int p, int end) {
    int i=p;
    int re = 0;
    while(true) {
        num[i]--;
        if(num[i]>=0) {
            break;
        } else {
            num[i] = 9;
            i--;
            re = i;
        }
    }

    for(i=p+1;i<end;i++) {
        num[i] = 9;
    }

    return max(1,re-1);
}




int main(int argc, char const *argv[]) {
    int tc;
    cin >> tc;
    getchar();

    for(int ti=1;ti<=tc;ti++) {
        int num[20]={};
        int end=0;
        char c;

        while(true) {
            c = getchar();
            if((c=='\n')||(c==EOF)) {
                break;
            }
            num[end] = c - '0';
            end++;
        }

        int i=1;
        while(i<end) {
            if(num[i-1]<=num[i]) {
                i++;
            } else {
                i = sub(num,i-1,end);
            }
        }

        cout << "Case #"<< ti <<": ";
        bool flag = false;
        for(int i=0;i<end;i++) {
            if((num[i]!=0)||(flag)) {
                flag = true;
                cout << num[i];
            }
        }

        cout << endl;



    }
    return 0;
}
