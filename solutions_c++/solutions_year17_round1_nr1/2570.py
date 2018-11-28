#include <iostream>
#include <cstdio>
#include <set>
#include <algorithm>
#include <iterator>
using namespace std;

int idx_in_set(set<char> unique_chars, char find) {
	int idx = 0;
	for (set<char>::iterator it=unique_chars.begin(); it!=unique_chars.end(); ++it) {
	    if (*it == find) {
	    	break;
	    }
	    else idx++;
	}
	return idx;
}

char char_at(set<char> unique_chars, int find) {
	int idx = 0;
	char retval = '?';
	for (set<char>::iterator it=unique_chars.begin(); it!=unique_chars.end(); ++it) {
	    if (idx==find) {
	    	retval = *it;
	    	break;
	    }
	    else idx++;
	}
	return retval;
}

void print(set<char> unique_chars) {
	for (set<char>::iterator it=unique_chars.begin(); it!=unique_chars.end(); ++it) {
	    cout << *it << " ";
	}
	cout << endl;
}

int main() {
	int t;
	scanf("%d",&t);
	for (int z=0; z<t; z++) {

		int r, c;		
		scanf("%d %d",&r,&c);
		string str[r];

		set<char> unique_chars;

		int fill = 0;
		for (int i=0; i<r; i++) {
			cin >> str[i];
			for (int j=0; j<c; j++) {
				if (str[i][j]!='?') {
					unique_chars.insert(str[i][j]);
				}
				else {
					fill++;
				}
			}
		}

		// int counting_c[c][unique_chars.size()];
		// int counting_r[r][unique_chars.size()];

		// for (int j=0; j<c; j++) {
		// 	for (int k=0; k<unique_chars.size(); k++) {
		// 		counting_c[j][k] = 0;
		// 	}
		// }
		// for (int i=0; i<r; i++) {
		// 	for (int k=0; k<unique_chars.size(); k++) {
		// 		counting_r[i][k] = 0;
		// 	}
		// }

		// int fill = 0;
		// for (int i=0; i<r; i++) {
		// 	for (int j=0; j<c; j++) {
		// 		if (str[i][j]!='?') {
		// 			// cout << str[i][j] << " " << idx_in_set(unique_chars, str[i][j]) << endl;
		// 			int idx = idx_in_set(unique_chars, str[i][j]);
		// 			counting_c[j][idx]++;
		// 			counting_r[i][idx]++;
		// 		}
		// 		else {
		// 			fill++;
		// 		}
		// 	}
		// } 
		// print(unique_chars);

		while (fill>0) {
			for (int i=0; i<r; i++) {
				for (int j=0; j<c; j++) {
					if (str[i][j]=='?') {
						// cout << "masuk " << i << " " << j << endl;
						bool solved = false;

						if (i-1>=0 && str[i-1][j]!='?') {
							// cout << "case 1" << endl;
							if (unique_chars.find(str[i-1][j])!=unique_chars.end()) {
								solved = true;
								int start_l = i-1;
								int start_m = j;
								
								//ke bawah
								int l = i;
								int m = j;
								while (l<r && str[l][m]=='?') {
									str[l][m] = str[l-1][m];
									fill--;
									l++;
								}
								l--;
								if (l==r) l--;

								//ke atas
								int end_l = start_l-1;
								bool executed = false;
								while (end_l>=0 && str[end_l][m]=='?') {
									str[end_l][m] = str[end_l+1][m];
									fill--;
									end_l--;
									executed = true;
								}
								end_l++;
								if (executed) start_l = min(end_l, start_l);
								if (start_l<0) start_l++;

								//ke kanan
								bool flag = true;
								while (flag) {
									if (m+1<c) {
										int bisa = 0;
										for (int p=start_l; p<=l; p++) {
											if (str[p][m+1]=='?') {
												bisa++;
											}
										}
										if (bisa==(l-start_l)+1) {
											//fill
											for (int p=start_l; p<=l; p++) {
												str[p][m+1] = str[p][m];
												fill--;
											}
										}
										else {
											flag = false;
										}
									}
									else {
										flag = false;
									}
									m++;
								}

								//ke kiri
								flag = true;
								m = start_m;
								while (flag) {
									if (m-1>=0) {
										int bisa = 0;
										for (int p=start_l; p<=l; p++) {
											if (str[p][m-1]=='?') {
												bisa++;
											}
										}
										if (bisa==(l-start_l)+1) {
											//fill
											for (int p=start_l; p<=l; p++) {
												str[p][m-1] = str[p][m];
												fill--;
											}
										}
										else {
											flag = false;
										}
									}
									else {
										flag = false;
									}
									m--;
								}
								// cout << "remove " << str[i][j] << endl;
								set<char>::iterator it = unique_chars.find (str[i][j]);
	  							unique_chars.erase (it);
	  							// print(unique_chars);
  							}
						}

						if (!solved && j-1>=0 && str[i][j-1]!='?') {
							// cout << "case 2" << endl;
							if (unique_chars.find(str[i][j-1])!=unique_chars.end()) {
								solved = true;
								int start_m = j-1;
								int start_l = i;
								//ke kanan
								int l = i;
								int m = j;
								while (m<c && str[l][m]=='?') {
									str[l][m] = str[l][m-1];
									fill--;
									m++;
								}
								m--;

								//ke kiri
								int end_m = start_m-1;
								bool executed = false;
								while (end_m>=0 && str[l][end_m]=='?') {
									str[l][end_m] = str[l][end_m+1];
									fill--;
									end_m--;
									executed = true;
								}
								end_m++;
								if (executed) start_m = min(start_m, end_m);
								if (start_m<0) start_m++;
								// cout << m << " " << start_m << endl;

								//ke bawah
								bool flag = true;
								while (flag) {
									if (l+1<r) {
										int bisa = 0;
										for (int p=start_m; p<=m; p++) {
											if (str[l+1][p]=='?') {
												bisa++;
											}
										}
										if (bisa==(m-start_m)+1) {
											//fill
											for (int p=start_m; p<=m; p++) {
												str[l+1][p] = str[l][p];
												fill--;
											}
										}
										else {
											flag = false;
										}
									}
									else {
										flag = false;
									}
									l++;
								}
								//ke atas
								flag = true;
								l = start_l;
								while (flag) {
									if (l-1>=0) {
										int bisa = 0;
										for (int p=start_m; p<=m; p++) {
											if (str[l-1][p]=='?') {
												bisa++;
											}
										}
										if (bisa==(m-start_m)+1) {
											//fill
											for (int p=start_m; p<=m; p++) {
												str[l-1][p] = str[l][p];
												fill--;
											}
										}
										else {
											flag = false;
										}
									}
									else {
										flag = false;
									}
									l--;
								}
								// cout << "remove " << str[i][j] << endl;
								set<char>::iterator  it = unique_chars.find (str[i][j]);
	  							unique_chars.erase (it);
	  							// print(unique_chars);
							}
						}

						if (!solved && j+1<c && str[i][j+1]!='?') {
							// cout << "case 3" << endl;
							if (unique_chars.find(str[i][j+1])!=unique_chars.end()) {
								solved = true;
								int start_m = j+1;
								int start_l = i;
								//ke kiri
								int l = i;
								int m = j;
								while (m>=0 && str[l][m]=='?') {
									str[l][m] = str[l][m+1];
									fill--;
									m--;
								}
								m++;

								//ke kanan
								int end_m = start_m+1;
								bool executed = false;
								while (end_m<c && str[l][end_m]=='?') {
									str[l][end_m] = str[l][end_m-1];
									fill--;
									end_m++;
									executed = true;
								}
								end_m--;
								if (executed) start_m = max(start_m, end_m);
								if (start_m==c) start_m--;

								//ke bawah
								bool flag = true;
								while (flag) {
									if (l+1<r) {
										int bisa = 0;
										for (int p=m; p<=start_m; p++) {
											if (str[l+1][p]=='?') {
												bisa++;
											}
										}
										if (bisa==(start_m-m)+1) {
											//fill
											for (int p=m; p<=start_m; p++) {
												str[l+1][p] = str[l][p];
												fill--;
											}
										}
										else {
											flag = false;
										}
									}
									else {
										flag = false;
									}
									l++;
								}
								//ke atas
								flag = true;
								l = start_l;
								while (flag) {
									if (l-1>=0) {
										int bisa = 0;
										for (int p=m; p<=start_m; p++) {
											if (str[l-1][p]=='?') {
												bisa++;
											}
										}
										if (bisa==(start_m-m)+1) {
											//fill
											for (int p=m; p<=start_m; p++) {
												str[l-1][p] = str[l][p];
												fill--;
											}
										}
										else {
											flag = false;
										}
									}
									else {
										flag = false;
									}
									l--;
								}
								// cout << "remove " << str[i][j] << endl;
								set<char>::iterator  it = unique_chars.find (str[i][j]);
	  							unique_chars.erase (it);
	  							// print(unique_chars);
  							}
						}

						if (!solved && i+1<r && str[i+1][j]!='?') {
							// cout << "case 4" << endl;
							if (unique_chars.find(str[i+1][j])!=unique_chars.end()) {
								solved = true;
								int start_l = i+1;
								int start_m = j;
								//ke atas
								int l = i;
								int m = j;
								while (l>=0 && str[l][m]=='?') {
									str[l][m] = str[l+1][m];
									fill--;
									l--;
								}
								l++;
								if (l<0) l++;

								//ke bawah
								int end_l = start_l+1;
								bool executed = false;
								while (end_l<r && str[end_l][m]=='?') {
									str[end_l][m] = str[end_l-1][m];
									fill--;
									end_l++;
									executed = true;
								}
								end_l--;
								if (executed) start_l = max(start_l, end_l);
								if (start_l==r) start_l--;

								//ke kanan
								bool flag = true;
								while (flag) {
									if (m+1<c) {
										int bisa = 0;
										for (int p=l; p<=start_l; p++) {
											if (str[p][m+1]=='?') {
												bisa++;
											}
										}
										if (bisa==(start_l-l)+1) {
											//fill
											for (int p=l; p<=start_l; p++) {
												str[p][m+1] = str[p][m];
												fill--;
											}
										}
										else {
											flag = false;
										}
									}
									else {
										flag = false;
									}
									m++;
								}
								//ke kiri
								flag = true;
								m = start_m;
								while (flag) {
									if (m-1>=0) {
										int bisa = 0;
										for (int p=l; p<=start_l; p++) {
											if (str[p][m-1]=='?') {
												bisa++;
											}
										}
										if (bisa==(start_l-l)+1) {
											//fill
											for (int p=l; p<=start_l; p++) {
												str[p][m-1] = str[p][m];
												fill--;
											}
										}
										else {
											flag = false;
										}
									}
									else {
										flag = false;
									}
									m--;
								}
								// cout << "remove " << str[i][j] << endl;
								set<char>::iterator it = unique_chars.find (str[i][j]);
	  							unique_chars.erase (it);
	  							// print(unique_chars);
  							}
						}
						// cout << "------------------" << endl;
						// for (int z=0; z<r; z++) {
						// 	cout << str[z] << endl;
						// }
						// cout << "------------------" << endl;
						// getchar();
					}
				}
			}
		}

		printf("Case #%d:\n",z+1);
		for (int i=0; i<r; i++) {
			cout << str[i] << endl;
		}
	}
	return 0;
}