#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

void divide(vector<vector<char> >& cake, int r, int c) {
    //vertical scan
    int cnt=0;
    for(int i=0;i<r;++i) {
        for(int j=0;j<c;++j) {
            if(cake[i][j]=='?') {
                cnt++;
                if(j>0 && cake[i][j-1]!='?') {
                    cake[i][j]=cake[i][j-1];
                    cnt--;
                }
                else if(j<c-1 && cake[i][j+1]!='?') {
                    cake[i][j]=cake[i][j+1];
                    cnt--;
                }
            }
        }
    }
    for(int i=r-1;i>=0;--i) {
        for(int j=c-1;j>=0;--j) {
            if(cake[i][j]=='?') {
                cnt++;
                if(j>0 && cake[i][j-1]!='?') {
                    cake[i][j]=cake[i][j-1];
                    cnt--;
                }
                else if(j<c-1 && cake[i][j+1]!='?') {
                    cake[i][j]=cake[i][j+1];
                    cnt--;
                }
            }
        }
    }
    if(cnt==0) return;
    //horizontal scan
    for(int i=0;i<r;++i) {
        for(int j=0;j<c;++j) {
            if(cake[i][j]=='?') {
                cnt++;
                if(i>0 && cake[i-1][j]!='?') {
                    cake[i][j]=cake[i-1][j];
                    cnt--;
                }
                else if(i<r-1 && cake[i+1][j]!='?') {
                    cake[i][j]=cake[i+1][j];
                    cnt--;
                }
            }
        }
    }
    for(int i=r-1;i>=0;--i) {
        for(int j=c-1;j>=0;--j) {
            if(cake[i][j]=='?') {
                cnt++;
                if(i>0 && cake[i-1][j]!='?') {
                    cake[i][j]=cake[i-1][j];
                    cnt--;
                }
                else if(i<r-1 && cake[i+1][j]!='?') {
                    cake[i][j]=cake[i+1][j];
                    cnt--;
                }
            }
        }
    }

}

int main() {
    
    ifstream infile;
    ofstream outfile;
    infile.open("r1.txt");
    outfile.open("out.txt");
    if(infile.is_open()) {
        int T; //# of cases
        infile>>T;
        for(int t=0;t<T;++t) {
            int r,c;
            infile>>r>>c;
            vector<vector<char> > cake;
            for(int i=0;i<r;++i) {
                vector<char> st;
                for(int j=0;j<c;++j) {
                    char c;
                    infile>>c;
                    st.push_back(c);
                }
                cake.push_back(st);
            }
            divide(cake,r,c);
            outfile<<"Case #"<<t+1<<":"<<endl;
            for(int i=0;i<r;++i) {
                for(int j=0;j<c;++j) {
                    outfile<<cake[i][j];
                }
                outfile<<endl;
            }
     
        }
    }
    infile.close();
    outfile.close();
    /*
    
    int T; //# of cases
    cin>>T;
    for(int t=0;t<T;++t) {
        int r,c;
        cin>>r>>c;
        if(r<1) return 0;
        vector<vector<char> > cake;
        for(int i=0;i<r;++i) {
            vector<char> st;
            for(int j=0;j<c;++j) {
                char c;
                cin>>c;
                st.push_back(c);
            }
            cake.push_back(st);
        }
        divide(cake,r,c);
        cout<<"Case #"<<t+1<<":"<<endl;
        for(int i=0;i<r;++i) {
            for(int j=0;j<c;++j) {
                cout<<cake[i][j];
            }
            cout<<endl;
        }

    }
    */
    return 0;
}
