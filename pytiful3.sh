#! /bin/sh

### BEGIN INIT INFO
# Provides:          pytiful3.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# I can't understand why volume will be loud

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting pytiful3.py"
    /usr/local/bin/pytiful3.py &
    ;;
  stop)
    echo "Stopping pytiful3.py"
    pkill -f /usr/local/bin/pytiful3.py
    ;;
  *)
    echo "Usage: /etc/init.d/pytiful3.sh {start|stop}"
    exit 1
    ;;
esac

exit 0

