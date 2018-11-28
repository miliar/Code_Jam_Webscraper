#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	int numCases;
	scanf("%d", &numCases);
	
	long long k, n;
	
	for (int i = 0 ; i < numCases ; ++i) {
	    scanf("%lld %lld", &n, &k);
	    
	    long long largeRoom      = n;
	    long long largeRoomCount = 1;
	    long long smallRoom      = n;
	    long long smallRoomCount = 0;
	    long long users          = 0;
	    long long depth          = 1L;
	    long long nextUsers      = 1L;
	    
	    // In case nextUsers overflow...
	    while (nextUsers < k || nextUsers < 0L) {
	        users       = nextUsers;
	        depth       *= 2L;
	        nextUsers   = users + depth;
	        
	        long long newLargeRoom = largeRoom - (1L + largeRoom) / 2L;
	        
	        long long newSmallRoom = (1L + smallRoom) / 2L - 1L;
	        newSmallRoom = (newSmallRoom < 0) ? 0 : newSmallRoom;
	        
	        long long newLargeRoomCount = 0;
	        long long newSmallRoomCount = 0;
	        
	        if (largeRoomCount > 0) {
	            long long newLL = largeRoom - (1L + largeRoom) / 2L;
	            long long newLS = (1L + largeRoom) / 2L - 1L;
	            newLS = (newLS < 0) ? 0 : newLS;
	            
	            newLargeRoomCount += (newLL == newLargeRoom) ? largeRoomCount : 0;	            
	            
				if (newLS == newLargeRoom) {
					newLargeRoomCount += largeRoomCount;
				}
				else {
					newSmallRoomCount += largeRoomCount;
				}	            
	        }
	        
	        if (smallRoomCount > 0) {
	            long long newSL = smallRoom - (1L + smallRoom) / 2L;
	            long long newSS = (1L + smallRoom) / 2L - 1L;
	            newSS = (newSS < 0) ? 0 : newSS;
				
				if (newSL == newLargeRoom) {
					newLargeRoomCount += smallRoomCount;
				}
				else {
					newSmallRoomCount += smallRoomCount;
				}
				
				if (newSS == newLargeRoom) {
					newLargeRoomCount += smallRoomCount;
				}
				else {
					newSmallRoomCount += smallRoomCount;
				}	            	            
	        }
	        
	        
	        largeRoom = newLargeRoom;
	        smallRoom = newSmallRoom;
	        largeRoomCount = newLargeRoomCount;
	        smallRoomCount = newSmallRoomCount;
	    }
	    
        // Choose from largeRoom
        if (k - users <= largeRoomCount) {
            long long l = largeRoom - (1L + largeRoom) / 2L;
            long long s = (1L + largeRoom) / 2L - 1L;
            s = (s < 0) ? 0 : s;
            printf("Case #%d: %lld %lld\n", i + 1, l, s);           
        }
        // Choose form smallRom
        else {
            long long l = smallRoom - (1L + smallRoom) / 2L;
            long long s = (1L + smallRoom) / 2L - 1L;
            s = (s < 0) ? 0 : s;
            printf("Case #%d: %lld %lld\n", i + 1, l, s);
        }
	}
	
	
	return 0;
}
