//Author: Andres-Felipe Ortega-Montoya
//D.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXN = 100;

int rows[4] = {-1, 0, 0, 1};
int cols[4] = {0, -1, 1, 0};

vector<string> board;
vector<pair<ii,ii> > nBoard;
vector<char> equiv;
int R,C;

bool intersecting(int l1, int l2){
  bool badr= false, badc = false;
  if((nBoard[l1].first.first == nBoard[l2].first.first)
     || (nBoard[l1].second.first == nBoard[l2].second.first)
     || (nBoard[l1].first.first == nBoard[l2].second.first)
     || (nBoard[l1].second.first == nBoard[l2].first.first)){
    //cout << "a1\n";
    badr = true;
  }
  if((nBoard[l1].first.second == nBoard[l2].first.second)
       || (nBoard[l1].second.second == nBoard[l2].second.second)
       || (nBoard[l1].first.second == nBoard[l2].second.second)
       || (nBoard[l1].second.second == nBoard[l2].first.second)){
    //cout << "a2\n";
    badc = true;
  }
  if((nBoard[l1].first.first < nBoard[l2].first.first)
     != (nBoard[l1].second.first < nBoard[l2].second.first)){
    //cout << "a3\n";
    //cout << (nBoard[l1].first.first < nBoard[l2].first.first) << " " << (nBoard[l1].second.first < nBoard[l2].second.first) << "\n";
    badr = true;
  }
  if((nBoard[l1].first.second < nBoard[l2].first.second)
     != (nBoard[l1].second.second < nBoard[l2].second.second)){
    //cout << "a4\n";
    badc= true;
  }
  return badr && badc;
}

void move(int letter){
  for(int i = 0; i < 4; ++i){
    if(i < 2){
      int oldr, oldc;
      while(true){
	oldr = nBoard[letter].first.first;
	oldc = nBoard[letter].first.second;
	nBoard[letter].first.first += rows[i];
	nBoard[letter].first.second += cols[i];
	if(nBoard[letter].first.first < 0 || nBoard[letter].first.first >= R
	   || nBoard[letter].first.second < 0 || nBoard[letter].first.second >= C)
	  break;
	bool good = true;
	for(int i = 0; i < nBoard.size(); ++i){
	  if(letter != i && intersecting(letter, i)){
	    /*cout << equiv[letter] << " " << nBoard[letter].first.first << " "
		 << nBoard[letter].first.second << " "
		 << nBoard[letter].second.first << " "
		 << nBoard[letter].second.second << "\n"
		 << equiv[i] << " " << nBoard[i].first.first << " "
		 << nBoard[i].first.second << " "
		 << nBoard[i].second.first << " "
		 << nBoard[i].second.second << "\n";*/
	    good = false;
	    break;
	  }
	}
	if(!good){
	  break;
	}
	//cout << equiv[letter] << " " << nBoard[letter].first.first << " " <<  nBoard[letter].first.second << " 1\n";
      }
      nBoard[letter].first.first = oldr;
      nBoard[letter].first.second = oldc;
      //cout << equiv[letter] << "* " << nBoard[letter].first.first << " " <<  nBoard[letter].first.second << " 1\n";
    }else{
      int oldr, oldc;
      while(true){
	oldr = nBoard[letter].second.first;
	oldc = nBoard[letter].second.second;
	nBoard[letter].second.first += rows[i];
	nBoard[letter].second.second += cols[i];
	if(nBoard[letter].second.first < 0 || nBoard[letter].second.first >= R
	   || nBoard[letter].second.second < 0 || nBoard[letter].second.second >= C)
	  break;
	bool good = true;
	for(int i = 0; i < nBoard.size(); ++i){
	  if(letter != i && intersecting(letter, i)){
	    /*cout << equiv[letter] << " " << nBoard[letter].first.first << " "
		 << nBoard[letter].first.second << " "
		 << nBoard[letter].second.first << " "
		 << nBoard[letter].second.second << "\n"
		 << equiv[i] << " " << nBoard[i].first.first << " "
		 << nBoard[i].first.second << " "
		 << nBoard[i].second.first << " "
		 << nBoard[i].second.second << "\n";*/
	    good = false;
	    break;
	  }
	}
	if(!good){
	  break;
	}
	//cout << equiv[letter] << " " << nBoard[letter].second.first << " " <<  nBoard[letter].second.second << " 2\n";
      }
      nBoard[letter].second.first = oldr;
      nBoard[letter].second.second = oldc;
      //cout << equiv[letter] << "* " << nBoard[letter].second.first << " " <<  nBoard[letter].second.second << " 2\n";
    }
  }
}

char zone(int r, int c){
  for(int i = 0; i < nBoard.size(); ++i){
    if(nBoard[i].first.first <= r && nBoard[i].second.first >= r
       && nBoard[i].first.second <= c && nBoard[i].second.second >= c)
      return equiv[i];
  }
  return '*';
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int TC;
  cin >> TC;
  for(int t = 1; t <= TC; ++t){
    board.clear();
    nBoard.clear();
    equiv.clear();
    cin >> R >> C;
    for(int r = 0; r < R; ++r){
      string temp;
      cin >> temp;
      board.push_back(temp);
    }
    for(int r = 0; r < R; ++r){
      for(int c = 0; c < C; ++c){
	if(board[r][c] != '?'){
	  nBoard.push_back({{r,c},{r,c}});
	  equiv.push_back(board[r][c]);
	}
      }
    }
    for(int i = 0; i < nBoard.size(); ++i){
      move(i);
    }
    cout << "Case #" << t << ":\n";
    for(int r = 0; r < R; ++r){
      for(int c = 0; c < C; ++c){
	cout << zone(r,c);
      }
      cout << "\n";
    }
  }
}
