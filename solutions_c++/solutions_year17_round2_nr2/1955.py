#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>

using namespace std;

string solve(int N, int R, int O, int Y, int G, int B, int V) {

   vector< pair<char, string> > seq;
   int newB = B;
   int newY = Y;
   int newR = R;
   string BOB;
   string YVY;
   string RGR;
   for (int i = 0; i < O; ++i) {
       if (BOB.empty()) {
           BOB = "B";
           newB--;
       }
       BOB = BOB + "OB";
       newB--;
   }

   for (int i = 0; i < V; ++i) {
       if (YVY.empty()) {
           YVY = "Y";
           newY--;
       }
       YVY = YVY + "VY";
       newY--;
   }

   for (int i = 0; i < G; ++i) {
       if (RGR.empty()) {
           RGR = "R";
           newR--;
       }
       RGR = RGR + "GR";
       newR--;
   }

   //cout << newR << " " << newY << " " << newB << endl;

   int negs = 0;
   char first;
   char last;
   string stalls;
   if (newR == -1 && N > G + R) return "IMPOSSIBLE";
   else if (newR == -1) {
       RGR.pop_back();
       return RGR;
   }
   if (newB == -1 && N > B + O) return "IMPOSSIBLE";
   else if (newB == -1) {
       BOB.pop_back();
       return BOB;
   }
   if (newY == -1 && N > Y + V) return "IMPOSSIBLE";
   else if (newY == -1) {
       YVY.pop_back();
       return YVY;
   }
   
   if (!BOB.empty()) newB++;
   if (!YVY.empty()) newY++;
   if (!RGR.empty()) newR++;

   if (newR >= newY && newR >= newB) last = 'R';
   else if (newY >= newB && newY >= newR) last = 'Y'; 
   else last = 'B';
   first = last;
   if (!BOB.empty() && last == 'B') {
       stalls += BOB;
       N -= BOB.size();
       BOB = "";
       newB--;
   } else if (!RGR.empty() && last == 'R') {
       stalls += RGR;
       N -= RGR.size();
       RGR = "";
       newR--;
   } else if (!YVY.empty() && last == 'Y') {
       stalls += YVY;
       N -= YVY.size();
       YVY = "";
       newY--;
   } else {
       stalls += last;
       N--;
        if (last == 'B') newB--;
        if (last == 'Y') newY--;
        if (last == 'R') newR--;
   }
   //cout << "init: " << stalls << "R " << newR << "Y:" << newY << "B: " << newB << endl;

   while (N != 0) {
     set<char> possible = {'R', 'Y', 'B'};
     possible.erase(last);

     if (newR == 0) possible.erase('R');
     if (newY == 0) possible.erase('Y');
     if (newB == 0) possible.erase('B');

     if (possible.size() == 0) return "IMPOSSIBLE";
     if (possible.find(first) != possible.end()) last = first;
     else {
         if (newR >= newY && newR >= newB && possible.find('R') != possible.end()) last = 'R';
         else if (newY >= newB && newY >= newR && possible.find('Y') != possible.end()) last = 'Y'; 
         else if (possible.find('B') != possible.end()) last = 'B';
         else last = *possible.begin();
     }

    if (!BOB.empty() && last == 'B') {
        stalls += BOB;
        N -= BOB.size();
        BOB = "";
        newB--;
    } else if (!RGR.empty() && last == 'R') {
        stalls += RGR;
        N -= RGR.size();
        RGR = "";
        newR--;
    } else if (!YVY.empty() && last == 'Y') {
        stalls += YVY;
        N -= YVY.size();
        YVY = "";
        newY--;
    } else {
        stalls += last;
        N--;
        if (last == 'B') newB--;
        if (last == 'Y') newY--;
        if (last == 'R') newR--;
    }
   }


   if (last == first) return "IMPOSSIBLE";
/*
   if (R == -1) {
       stalls += "RG";
   } else if (B == -1) {
       stalls += "BO";
   } else if (Y == -1) {
       stalls += "YV";
   }
*/
   return stalls;
}

int main() {

    ofstream fout;
    fout.open("output.txt");

    if (fout.is_open()) {
        int N, R, O, Y, G, B, V;

        int num_tests = 0;
        cin >> num_tests;

        unsigned count = 1;
        while ( count <= num_tests ) {
            cin >> N >> R >> O >> Y >> G >> B >> V;
            fout << "Case #" << count << ": ";
            fout << solve(N, R, O, Y, G, B, V) << endl; 
            count++;
        }
        fout.close();
    } else {
        cout << "Can't open file!";
    }
    return 0;
}