/*
 * A.cpp
 *
 *  Created on: 11 Apr 2016
 *      Author: xing
 */


#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <unordered_set>
#include <unordered_map>

using namespace std;

//#define DEBUG

struct Rec{
	int left, right, top, bottom;
	//Rec(int _l, int _r, int _t, int _b):left(_l), right(_r), top(_t), bottom(_b){}
	Rec(){
		left = top = 100;
		right = bottom = -1;
	}
};

void solve(int index){
	int r, c;
	string line;

	cin>>r>>c;
	getline(cin, line);

	vector< vector<char> > board(r, vector<char>());
	for(int i = 0;i<r;i++){
		getline(cin, line);
		for(auto&& ch:line)
			board[i].push_back(ch);
	}


	Rec names[26];

	for(int i = 0;i<r;i++){
		for(int j = 0;j<c;j++){
			if(board[i][j] == '?')
				continue;

			names[board[i][j]-'A'].left = min(names[board[i][j]-'A'].left, j);
			names[board[i][j]-'A'].right = max(names[board[i][j]-'A'].right, j);
			names[board[i][j]-'A'].top = min(names[board[i][j]-'A'].top, i);
			names[board[i][j]-'A'].bottom = max(names[board[i][j]-'A'].bottom, i);
		}
	}

#ifdef DEBUG
	cout<<"after cal pos"<<endl;
#endif

	for(int k = 0;k<26;k++){
		if(names[k].left == 100)
			continue;
		for(int i = names[k].top;i<=names[k].bottom;i++){
			for(int j = names[k].left;j<=names[k].right;j++){
				board[i][j] = 'A'+k;
			}
		}
	}

	for(int i = 0;i<r;i++){
		for(int j = 0;j<c;j++){
			if(board[i][j] != '?')
				continue;
			for(int k = 0;k<26;k++){
				if(names[k].left == 100)
					continue;
				bool feasible = true;
				for(int inneri = min(i, names[k].top);inneri<=max(i, names[k].bottom); ++inneri){
					for(int innerj =min(j, names[k].left); innerj<=max(j, names[k].right);++innerj){
						if(board[inneri][innerj]!='?'&&board[inneri][innerj]!='A'+k){
							feasible = false;
							break;
						}
					}
					if(!feasible)
						break;
				}

				if(feasible){
					for(int inneri = min(i, names[k].top);inneri<=max(i, names[k].bottom); ++inneri){
						for(int innerj =min(j, names[k].left); innerj<=max(j, names[k].right);++innerj){
							board[inneri][innerj] = 'A'+k;
						}
					}
					names[k].top = min(i, names[k].top);
					names[k].bottom = max(i, names[k].bottom);
					names[k].left = min(j, names[k].left);
					names[k].right = max(j, names[k].right);
					break;
				}
			}
		}
	}


	cout<<"Case #"<<index<<": "<<endl;
	for(auto&& row:board){
		for(auto&& cell:row)
			cout<<cell;
		cout<<endl;
	}


}

int main(){
	int T;

	cin>>T;
	for(int i = 0;i<T;i++){
		solve(i+1);
	}

}
