#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <iomanip>

using namespace std;

string smallcase(int R, int B, int Y)
{
    string sBiggest = "";
    string sMiddle = "";
    string sSmall = "";
    int iBiggest = 0;
    int iMiddle = 0;
    int iSmall = 0;
    if (R >= B && R >= Y){
        sBiggest = "R";
        iBiggest = R;
        if(B >= Y){
            sMiddle = "B";
            sSmall = "Y";
            iMiddle = B;
            iSmall = Y;
        }
        else{
            sMiddle = "Y";
            sSmall = "B";
            iMiddle = Y;
            iSmall = B;
        }
    }
    else if (B >= R && B >= Y){
        sBiggest = "B";
        iBiggest = B;
        if(R >= Y){
            sMiddle = "R";
            sSmall = "Y";
            iMiddle = R;
            iSmall = Y;
        }
        else{
            sMiddle = "Y";
            sSmall = "R";
            iMiddle = Y;
            iSmall = R;
        }
    }
    else if(Y >= B && Y >= R){
        sBiggest = "Y";
        iBiggest = Y;
        if(R >= B){
            sMiddle = "R";
            sSmall = "B";
            iMiddle = R;
            iSmall = B;
        }
        else{
            sMiddle = "B";
            sSmall = "R";
            iMiddle = B;
            iSmall = R;
        }
    }

    if(iBiggest > iMiddle + iSmall)
        return "IMPOSSIBLE";

    string res = "";

    for(int i = 0; i < iBiggest; i++){
        res += sBiggest;
    }
    for(int j = 0; j < iMiddle; j++){
        res.insert(2*j+1,sMiddle);
    }
    int last = iBiggest + iMiddle;
    for(int i = 0; i < iSmall; i++){
        res.insert(last - i,sSmall);
    }
    return res;
}

int main()
{
    string inname = "B-small-attempt0.in";
    string outname = "B-small-attempt0.out";
    ifstream infile(inname);
    ofstream outfile(outname);
    int T = 0;
    infile >> T;
    for(int k = 1; k <= T; k++)
    {
        int N = 0, R = 0, O = 0, Y = 0, G = 0, B = 0, V = 0;
        infile >> N >> R >> O >> Y >> G >> B >> V;
        string res = smallcase(R,B,Y);
        outfile << "Case #" << k << ": " << res;
        if(k < T)
            outfile << endl;
    }

    infile.close();
    outfile.close();

    return 0;
}
