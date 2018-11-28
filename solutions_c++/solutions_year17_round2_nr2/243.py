#include<iostream>
#include<algorithm>
#include<string>
#include<utility>
using namespace std;

string solve2(int b, int r, int y){
   pair<int, string> V[3];
   V[0] = make_pair(b, "B");
   V[1] = make_pair(r, "R");
   V[2] = make_pair(y, "Y");
   sort(V,V+3);
   reverse(V, V+3);
   //cerr << V[0].first << " " << V[1].first << " " << V[2].first << endl;
   if(V[0].first > V[1].first + V[2].first){
      return "IMPOSSIBLE";
   }
   string ret = "";
   while(V[0].first < V[1].first + V[2].first){
      ret += V[0].second;
      ret += V[1].second;
      ret += V[2].second;
      V[0].first--; V[1].first--; V[2].first--;
   }
   while(V[1].first > 0){
      ret += V[0].second;
      ret += V[1].second;
      V[0].first--; V[1].first--;
   }
   while(V[2].first > 0){
      ret += V[0].second;
      ret += V[2].second;
      V[0].first--; V[2].first--;
   }
   return ret;
}

string solve(){
   int N;
   cin >> N;
   int R,O,Y,G,B,V;
   cin >> R >> O >> Y >> G >> B >> V;
   string ret = "";
   if(R == 0 and Y == 0 and G == 0 and V == 0){
      if(B == O){
	 for(int i = 0; i < O; i++){
	    ret += "BO";
	 }
	 return ret;
      }
      else{
	 return "IMPOSSIBLE";
      }
   }
   if(Y == 0 and B == 0 and V == 0 and O == 0){
      if(G == R){
	 for(int i = 0; i < G; i++){
	    ret += "RG";
	 }
	 return ret;
      }
      else{
	 return "IMPOSSIBLE";
      }
   }
   if(R == 0 and B == 0 and O == 0 and G == 0){
      if(V == Y){
	 for(int i = 0; i < V; i++){
	    ret += "YV";
	 }
	 return ret;
      }
      else{
	 return "IMPOSSIBLE";
      }
   }

   if((O != 0 and B <= O) or (G != 0 and R <= G) or (V != 0 and Y <= V)){
      return "IMPOSSIBLE";
   }
   string simple = solve2(B-O, R-G, Y-V);
   if(simple == "IMPOSSIBLE")
      return "IMPOSSIBLE";
   bool fr=false,fb=false,fy=false;
   for(int i = 0; i < (int)simple.length(); i++){
      if(simple[i] == 'R' and !fr){
	 fr = true;
	 for(int j = 0; j < G; j++){
	    ret += "RG";
	 }
      }
      else if(simple[i] == 'B' and !fb){
	 fb = true;
	 for(int j = 0; j < O; j++){
	    ret += "BO";
	 }
      }
      else if(simple[i] == 'Y' and !fy){
	 fy = true;
	 for(int j = 0; j < V; j++){
	    ret += "YV";
	 }
      }
      ret += simple[i];
   }
   return ret;
}

int main(){
   int T;
   cin >> T;
   for(int c = 1; c <= T; c++){
      cout << "Case #" << c << ": " << solve() << endl;
   }
   return 0;
}
