
#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

int grd[52];

int w[52][1000005];


int main(int argc, char *argv[])
{
   std::ios::sync_with_stdio(false);
   int T, D, N, K, S;
   int ca = 0;

   cin >> T;
   while(ca < T)
   {
       double mt = 0.0;
       cin >> D >> N;
       for(int i = 0; i < N ; ++i)
       {
           cin >> K >> S;
           mt = max(mt, double(D-K)/double(S));
       }
       ca++;
       cout << "Case #" <<ca << ": " << setprecision(8) <<double(D)/mt << "\n";
   }
   return 0;
}










//char grid[26][26];
//vector<pair<int, int>> data;

//int main(int argc, char *argv[])
//{
//   std::ios::sync_with_stdio(false);
//   int T;
//   cin >> T;
//   int c = 0;
//   string dummy;
//   while(c<T)
//   {
//       int R,C;
//       cin >> R >> C;

//       getline(cin, dummy);
//       for(int i = O; i < R; i++)
//           for (int j = 0; j < C;j++)
//           {
//               char ch;
//               cin >> ch;
//               if (ch >= 'A' && ch <= 'Z')
//               {
//                   grid[i][j] = ch;
//                   pair<int, int> p = {i,j};
//                   data.push_back(p);
//               }
//           }
//       vector<pair<int, int>>::iterator it = data.begin();
//       //pair<int, int> or = {0 , 0};
//       pair<int, int> en = {R-1,C-1};

//       //data.insert(it,or);
//       data.push_back(en);

//       std::sort(data.begin(), data.end());
//       int lastR = 0;
//       int currR = 0;
//       for (int _i = 0; _i < data.size() -1; _i++)
//       {
//           currR = data[_i].first;
//           vector<int> vi;
//           vi.push_back(0);

//           while(data[_i] == currR)
//           {
//               vi.push_back(data[_i].second);
//           }
//           vi.push_back(C);

//           for (int i = 0; i < )

//       }

//       c++;
//       cout << "Case #" << c << ":\n";

//   }



//   while(getline(cin, line))
//   {
//       stringstream ss(line);
//       int l; ss >> l;

//       getline(cin, line);
//       stringstream ss2(line);
//       //vector<string> vs;
//       string ts;
//       string last = "+x";
//       while(ss2 >> ts)
//       {
//           if(ts!= "No")
//           {
//              if(last = "+x")
//                  last = ts;
//              else if (last = "-x")
//              {
//                  if (ts == '+y') last = "-y";
//                  else if (ts == "-y") last = "+y";
//                  else if (ts == '+z') last = "-z";
//                  else if (ts == '-z') last = "+z";
//              }
//              else if()

//           }



//       }
//   }
//   return 0;
//}
